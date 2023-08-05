#!env python3

import collections

import pycollimator.model_builder.core as core
from pycollimator.model_builder.model import ModelBuilder


def parse_json(data):
    uuids = {}
    uiprops = {}
    root_model_builder = ModelBuilder(data["name"])
    uuids[root_model_builder.id] = data["uuid"]
    core_vars = vars(core)

    nodes = {}

    # FIXME: reference Submodels have parameters too.
    for key, val in data["parameters"].items():
        root_model_builder.add_parameter(key, val["value"])

    def parse_diagram(model_builder, diagram):
        for node in diagram["nodes"]:
            params = {param_name: param_data["value"] for param_name, param_data in node["parameters"].items()}
            node_type = "".join(node["type"].split(".")[1:])

            if node_type in ("Submodel", "Group"):
                params["input_names"] = tuple(i["name"] for i in node["inputs"])
                params["output_names"] = tuple(i["name"] for i in node["outputs"])
            elif node_type == "ReferenceSubmodel":
                params["input_names"] = tuple(i["name"] for i in node["inputs"])
                params["output_names"] = tuple(i["name"] for i in node["outputs"])

            node_obj = core_vars[node_type](model=model_builder, name=node["name"], **params)
            nodes[node["uuid"]] = node_obj
            uuids[node_obj.id] = node["uuid"]
            uiprops[node_obj.id] = node["uiprops"]

            if node_type in ("Submodel", "Group"):
                diagram_uuid = data["submodels"]["references"][node["uuid"]]["diagram_uuid"]
                submodel_builder = ModelBuilder(node["name"])
                parse_diagram(submodel_builder, data["submodels"]["diagrams"][diagram_uuid])
                model_builder.add_diagram(nodes[node["uuid"]], submodel_builder)

        node_inputs = collections.defaultdict(list)
        for link in diagram["links"]:
            src_node = nodes[link["src"]["node"]]
            src_port_id = link["src"]["port"]
            dst_node = nodes[link["dst"]["node"]]
            dst_port_id = link["dst"]["port"]
            node_inputs[dst_node].append((src_node, src_port_id))
            out_port = src_node.output_port(src_port_id)
            in_port = dst_node.input_port(dst_port_id)
            l = model_builder.add_link(out_port, in_port)
            uuids[l.id] = link["uuid"]
            uiprops[l.id] = link["uiprops"]

    parse_diagram(root_model_builder, data["diagram"])
    return root_model_builder, uuids, uiprops
