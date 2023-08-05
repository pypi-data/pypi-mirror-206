from collections import defaultdict
import functools


class _PythonCode:
    def __init__(self):
        self.vars = {}
        self.var_ids = defaultdict(int)
        self.lines = []

    def write(self, line: str):
        self.lines.append(line)

    def __repr__(self):
        return "\n".join(self.lines)


def process_args(args, model_vars):
    new_args = []
    for a in args:
        if type(a) is str:
            new_args.append(f'"{a}"')
        elif a in model_vars:
            new_args.append(model_vars[a])
        elif isinstance(a, tuple):
            v = []
            if hasattr(a, "_fields"):
                # Named tuples
                for field_name in a._fields:
                    field_value = getattr(a, field_name)
                    if field_value in model_vars:
                        v.append(model_vars[field_value])
                    elif type(field_value) is str:
                        v.append(f'"{field_value}"')
                    else:
                        v.append(field_value)
                v = ", ".join([str(x) for x in v])
                new_args.append(f"{a.__class__.__name__}({v})")
            else:
                pa = process_args(a, model_vars)
                if len(pa) > 0:
                    t = ", ".join(pa)
                    new_args.append(f"({t},)")
                else:
                    new_args.append("None")
        else:
            new_args.append(a)

    return new_args


def process_kwargs(args, model_vars):
    vals = process_args(args.values(), model_vars)
    return dict(zip(args.keys(), vals))


class Recorder:
    enabled = False
    python_code = _PythonCode()

    @classmethod
    def output(cls, indent=0):
        code = [f"{' '*indent}{l}" for l in Recorder.python_code.lines]
        return "\n".join(code)

    def record_call(func):
        """record_call assumes that func is called with self as first argument"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not Recorder.enabled:
                return func(*args, **kwargs)

            if args[0] not in Recorder.python_code.vars:
                varname = args[0].__class__.__name__.lower()
                Recorder.python_code.vars[args[0]] = args[0].id
                Recorder.python_code.var_ids[varname] += 1

            unnamed_args = process_args(args, Recorder.python_code.vars)
            named_args = process_kwargs(kwargs, Recorder.python_code.vars)

            # Convert all to string
            unnamed_args = [str(a) for a in unnamed_args]
            named_args = [f"{k}={v}" for k, v in named_args.items()]

            class_name = args[0].__class__.__name__
            call_str = []

            # Skip self
            unnamed_args = unnamed_args[1:]

            if func.__name__ == "__init__":
                func_name = class_name
                # assign to variable
                call_str.append(f"{Recorder.python_code.vars[args[0]]} = ")
                named_args += [f'id="{args[0].id}"']
            else:
                func_name = func.__name__
                # if function is class member
                call_str.append(f"{Recorder.python_code.vars[args[0]]}.")

            all_args = unnamed_args + named_args
            all_args = ", ".join(all_args)
            call_str.append(f"{func_name}({all_args})")

            Recorder.python_code.write(f"{''.join(call_str)}")

            return func(*args, **kwargs)

        return wrapper
