from lxml import etree
from typing import Any, Dict

NS = "http://librml.org/schema"
NS_MAP = {None: NS}

BOOLEAN_FIELDS = {
    "mention", "sharealike", "commercialuse", "copyright",
    "permission", "required"
}
INTEGER_FIELDS = {
    "minage", "maxage", "maxbitrate", "maxdimension", "maxresolution",
    "count", "maxduration", "percentage", "sessions"
}
LIST_FIELDS = {
    "groups", "inside", "outside"
}

def _to_bool(value: str) -> bool:
    return value.lower() in ("true", "1")

def _from_bool(value: bool) -> str:
    return "true" if value else "false"

def xml_to_json(xml_content: bytes) -> Dict[str, Any]:
    root = etree.fromstring(xml_content)
    # The XSD says libRML has one 'item'
    item_el = root.find(f"{{{NS}}}item")
    if item_el is None:
        # Fallback if no namespace or different structure (though XSD says it should be there)
        item_el = root.find("item")

    if item_el is None:
        return {}

    result = {}

    # Item attributes
    for attr, val in item_el.attrib.items():
        if attr in BOOLEAN_FIELDS:
            result[attr] = _to_bool(val)
        else:
            result[attr] = val

    # Actions
    actions = []
    for action_el in item_el.findall(f"{{{NS}}}action"):
        action = {}
        for attr, val in action_el.attrib.items():
            if attr in BOOLEAN_FIELDS:
                action[attr] = _to_bool(val)
            else:
                action[attr] = val

        # Restrictions
        restrictions = []
        for rest_el in action_el.findall(f"{{{NS}}}restriction"):
            restriction = {}
            for attr, val in rest_el.attrib.items():
                if attr in BOOLEAN_FIELDS:
                    restriction[attr] = _to_bool(val)
                elif attr in INTEGER_FIELDS:
                    restriction[attr] = int(val)
                elif attr in LIST_FIELDS:
                    restriction[attr] = val.split()
                else:
                    restriction[attr] = val
            restrictions.append(restriction)

        if restrictions:
            action["restrictions"] = restrictions
        actions.append(action)

    if actions:
        result["actions"] = actions

    return result

def json_to_xml(json_data: Dict[str, Any], version: str = "0.5.0") -> bytes:
    root = etree.Element(f"{{{NS}}}libRML", version=version, nsmap=NS_MAP)
    item_el = etree.SubElement(root, f"{{{NS}}}item")

    # Process item properties
    for key, value in json_data.items():
        if key == "actions":
            continue

        if value is None:
            continue

        if key in BOOLEAN_FIELDS:
            item_el.set(key, _from_bool(value))
        else:
            item_el.set(key, str(value))

    # Process actions
    if "actions" in json_data:
        for action_data in json_data["actions"]:
            action_el = etree.SubElement(item_el, f"{{{NS}}}action")
            for key, value in action_data.items():
                if key == "restrictions":
                    continue
                if key in BOOLEAN_FIELDS:
                    action_el.set(key, _from_bool(value))
                else:
                    action_el.set(key, str(value))

            # Process restrictions
            if "restrictions" in action_data:
                for rest_data in action_data["restrictions"]:
                    rest_el = etree.SubElement(action_el, f"{{{NS}}}restriction")
                    for rkey, rvalue in rest_data.items():
                        if rkey in BOOLEAN_FIELDS:
                            rest_el.set(rkey, _from_bool(rvalue))
                        elif rkey in INTEGER_FIELDS:
                            rest_el.set(rkey, str(rvalue))
                        elif rkey in LIST_FIELDS:
                            if isinstance(rvalue, list):
                                rest_el.set(rkey, " ".join(rvalue))
                            else:
                                rest_el.set(rkey, str(rvalue))
                        else:
                            rest_el.set(rkey, str(rvalue))

    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
