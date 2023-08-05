import pycollimator.model_builder.model as model
import pycollimator.model_builder.schema_reader as schema_reader


SCHEMAS = {}
CLASSES = {}

for s in schema_reader.load_schemas("core"):
    klass = model._node_class_from_schema(s)
    SCHEMAS[s.name] = s
    CLASSES[s.name] = klass
    globals()[s.name] = klass


class Integrator(Integrator):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_reset") == "true":
                if "reset" not in ins:
                    ins += ("reset",)
                if params.get("enable_external_reset", "true") == "true":
                    if "reset_value" not in ins:
                        ins += ("reset_value",)
            if params.get("enable_hold") == "true":
                if "hold" not in ins:
                    ins += ("hold",)
            if params.get("enable_limits") == "true":
                if "upper_limit" not in ins:
                    ins += ("upper_limit", "lower_limit")
            params["input_names"] = ins
        super().__init__(**params)


class IntegratorDiscrete(IntegratorDiscrete):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_reset") == "true":
                if "reset" not in ins:
                    ins += ("reset",)
                if params.get("enable_external_reset") == "true":
                    if "reset_value" not in ins:
                        ins += ("reset_value",)
            if params.get("enable_hold") == "true":
                if "hold" not in ins:
                    ins += ("hold",)
            if params.get("enable_limits") == "true":
                if "upper_limit" not in ins:
                    ins += ("upper_limit", "lower_limit")
            params["input_names"] = ins
        super().__init__(**params)


class PID(PID):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_external_initial_state") == "true":
                if "initial_state" not in ins:
                    ins += ("initial_state",)
            params["input_names"] = ins
        super().__init__(**params)


class PID_Discrete(PID_Discrete):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_external_initial_state") == "true":
                if "initial_state" not in ins:
                    ins += ("initial_state",)
            params["input_names"] = ins
        super().__init__(**params)


class LogicalOperator(LogicalOperator):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = (
                "in_0",
                "in_1",
            )
            if params.get("function") == "not":
                ins = ("in_0",)
            params["input_names"] = ins
        super().__init__(**params)


class RateLimiter(RateLimiter):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_dynamic_upper_limit") == "true":
                if "upper_limit" not in ins:
                    ins += ("upper_limit",)
            if params.get("enable_dynamic_lower_limit") == "true":
                if "lower_limit" not in ins:
                    ins += ("lower_limit",)
            params["input_names"] = ins
        super().__init__(**params)


class Saturate(Saturate):
    def __init__(self, **params):
        if "input_names" not in params:
            ins = ("in_0",)
            if params.get("enable_dynamic_upper_limit") == "true":
                if "upper_limit" not in ins:
                    ins += ("upper_limit",)
            if params.get("enable_dynamic_lower_limit") == "true":
                if "lower_limit" not in ins:
                    ins += ("lower_limit",)
            params["input_names"] = ins
        super().__init__(**params)


# class Adder(Adder):
#     def __init__(self, **params):
#         ins = [f"in_{k}" for k in range(len(params["operators"]))]
#         super().__init__(input_names=tuple(ins), **params)
