import argparse
import json

from pycollimator.model_builder import to_json
from pycollimator.model_builder.core import *
from pycollimator.model_builder.model import ModelBuilder, OPort, IPort


def create_model():
    ModelBuilder_0 = ModelBuilder("Simple Dynamic System", id="ModelBuilder_0")
    Integrator_0 = Integrator(
        model=ModelBuilder_0,
        name="Integrator",
        enable_hold="false",
        enable_limits="false",
        enable_reset="false",
        hold_trigger_method="high",
        initial_states="0",
        lower_limit="-1e50",
        reset_trigger_method="rising",
        upper_limit="1.0e50",
        input_names=("in_0",),
        id="Integrator_0",
    )
    Gain_0 = Gain(model=ModelBuilder_0, name="Gain", gain="2", id="Gain_0")
    ModelBuilder_0.add_link(OPort(Integrator_0, "out_0"), IPort(Gain_0, "in_0"))
    ModelBuilder_0.add_link(OPort(Gain_0, "out_0"), IPort(Integrator_0, "in_0"))
    return ModelBuilder_0


if __name__ == "__main__":
    """
    Takes a Python model and converts it to JSON. The input
    python code should contain a `create_model` function that
    returns a ModelBuilder object.

    Usage:
        bazel run //src/lib/pycollimator/model_builder/tools:python_to_json -- example_model.py
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path", type=str, help="path to Python model file")
    args = parser.parse_args()

    with open(args.model_path) as f:
        exec(f.read(), globals(), locals())

        model = create_model()
        print(json.dumps(to_json.render_model(model), indent=2))
