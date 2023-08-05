#!/usr/bin/env python3

import pycollimator.model_builder.id as id


def _autolayout(model):
    uiprops = {}

    h_spacing = 100
    v_spacing = 100

    def _process_node(node, x, y):
        uiprops[node.id] = {
            "x": x,
            "y": y,
        }

        # layout all incoming nodes
        n_input = len(node.input_names)
        start_y = y - (n_input - 1) * v_spacing / 2
        for i in range(n_input):
            inport = node.input_port(i)
            if inport not in model.links:
                raise ValueError("Input port not connected")

            in_node = model.links[inport].dst.node
            if in_node.id in uiprops:
                continue
            uiprops[in_node.id] = {
                "x": x - h_spacing,
                "y": start_y + i * v_spacing,
            }

    x, y = 0, 0
    for node in model.nodes.values():
        if node.id in uiprops:
            continue
        _process_node(node, x, y)
        x += 100

    for link in model.links.values():
        uiprops[link.id] = {
            "link_type": {"connection_method": "direct_to_block"},
            "segments": [],
        }

    return uiprops


def render_diagram(model, uiprops):
    if uiprops is None:
        uiprops = _autolayout(model)
    return {
        "nodes": [render_node(node, uiprops[node.id]) for node in model.nodes.values()],
        "links": [render_link(l, uiprops[l.id]) for l in model.links.values()],
        "annotations": [],
    }


def render_model(model, uuids=None, uiprops=None):
    if uuids:
        id.Id.set_uuid_mapping(uuids)

    diagrams = {}
    references = {}

    for node, submodel in model.submodels.items():
        diagrams[submodel.uuid] = render_diagram(submodel, uiprops)
        references[node.uuid] = {"diagram_uuid": submodel.uuid}

    return {
        "name": model.name,
        "uuid": model.uuid,
        "diagram": render_diagram(model, uiprops),
        "submodels": {
            "diagrams": diagrams,
            "references": references,
        },
        "parameters": {k: {"value": v} for k, v in model.parameters.items()},
        "configuration": model.configuration or {},
    }


def render_node(node, uiprops):
    parameters = {}
    for k, v in node.params.items():
        # print("node", k, v)
        # print("defs", node.schema.parameter_definitions[k])
        if k not in node.schema.parameter_definitions:
            continue
        if node.schema.parameter_definitions[k].get("data_type", "any") == "string":
            parameters[k] = {"value": str(v), "is_string": True}
        else:
            # parameters[k] = {"value": repr(v)}
            parameters[k] = {"value": str(v)}

    return {
        "name": node.name,
        "uuid": node.uuid,
        "type": node.typename,
        "inputs": [
            # Note: not including kind, not useful
            {"name": name}
            for name in node.input_names
        ],
        "outputs": [
            # Note: not including kind, not useful
            {"name": name}
            for name in node.output_names
        ],
        "parameters": parameters,
        "uiprops": uiprops,
    }


def render_link(link, uiprops):
    src, dst = link.src, link.dst
    return {
        "uuid": link.uuid,
        "name": f"{src.node.name}.{src.name} -> {dst.node.name}.{dst.name}",
        "src": {
            "node": src.node.uuid,
            "port": src.index,
            "node_name": src.node.name,
            "port_name": src.name,
        },
        "dst": {
            "node": dst.node.uuid,
            "port": dst.index,
            "node_name": dst.node.name,
            "port_name": dst.name,
        },
        "uiprops": uiprops,
    }
