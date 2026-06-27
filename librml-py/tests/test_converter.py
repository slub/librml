from librml.converter import json_to_xml, xml_to_json


def test_xml_to_json_conversion():
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<libRML version="0.5.0" xmlns="http://librml.org/schema">
  <item id="test-1" copyright="true">
    <action type="read" permission="true">
      <restriction type="age" minage="18"/>
    </action>
  </item>
</libRML>
"""
    result = xml_to_json(xml)
    assert result["id"] == "test-1"
    assert result["copyright"] is True
    assert len(result["actions"]) == 1
    action = result["actions"][0]
    assert action["type"] == "read"
    assert action["permission"] is True
    assert len(action["restrictions"]) == 1
    restriction = action["restrictions"][0]
    assert restriction["type"] == "age"
    assert restriction["minage"] == 18


def test_json_to_xml_conversion():
    data = {
        "id": "test-2",
        "commercialuse": False,
        "actions": [
            {
                "type": "download",
                "permission": True,
                "restrictions": [{"type": "location", "inside": "Germany"}],
            }
        ],
    }
    xml_bytes = json_to_xml(data)
    assert b'id="test-2"' in xml_bytes
    assert b'commercialuse="false"' in xml_bytes
    assert b'type="download"' in xml_bytes
    assert b'permission="true"' in xml_bytes
    assert b'type="location"' in xml_bytes
    assert b'inside="Germany"' in xml_bytes


def test_bidirectional_consistency():
    original_json = {
        "id": "test-3",
        "actions": [
            {
                "type": "print",
                "permission": True,
                "restrictions": [{"type": "count", "count": 5}],
            }
        ],
    }
    xml_bytes = json_to_xml(original_json)
    converted_json = xml_to_json(xml_bytes)

    # We might have extra fields like version in XML that are not in original_json
    # but the core data should be the same.
    assert converted_json["id"] == original_json["id"]
    assert converted_json["actions"] == original_json["actions"]
