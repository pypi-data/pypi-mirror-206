import argparse
import json

from pycollimator.model_builder.call_recorder import Recorder
from pycollimator.model_builder import from_json


_TEMPLATE = """
from core import *
from model import ModelBuilder, OPort, IPort

def create_model():
{}
    return ModelBuilder_0
"""


if __name__ == "__main__":
    """
    Usage:
        bazel run //src/lib/pycollimator/model_builder/tools:json_to_python -- models/double_bouncing_ball.json
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="path to JSON file")
    args = parser.parse_args()

    with open(args.filepath) as f:
        in_json_data = json.load(f)

        Recorder.enabled = True
        model_builder, uuids, uiprops = from_json.parse_json(in_json_data)

        print(_TEMPLATE.format(Recorder.output(indent=4)))
