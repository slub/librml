import json
import warnings
from pathlib import Path
from typing import Optional, Union

from lxml import etree
from jsonschema import validate as validate_json_schema
from jsonschema.exceptions import ValidationError as JSONValidationError

class LibRMLValidator:
    def __init__(self):
        self.schema_dir = Path(__file__).parent.resolve() / "schemas"
        self.xsd_path = self.schema_dir / "librml.xsd"
        self.json_schema_path = self.schema_dir / "librml.json"

        if not self.xsd_path.exists():
            raise FileNotFoundError(f"XSD schema not found at {self.xsd_path}")
        if not self.json_schema_path.exists():
            raise FileNotFoundError(f"JSON schema not found at {self.json_schema_path}")

        with open(self.xsd_path, "rb") as f:
            schema_doc = etree.parse(f)
            self.xsd = etree.XMLSchema(schema_doc)
            # Extract version from XSD root element attribute
            self.xsd_version = schema_doc.getroot().get("version")

        with open(self.json_schema_path, "r") as f:
            self.json_schema = json.load(f)

    def validate_xml(self, xml_content: Union[str, bytes, Path]) -> tuple[bool, Optional[str]]:
        try:
            if isinstance(xml_content, Path):
                doc = etree.parse(str(xml_content))
            elif isinstance(xml_content, str):
                doc = etree.fromstring(xml_content.encode("utf-8"))
            else:
                doc = etree.fromstring(xml_content)

            # Check for version mismatch
            root = doc.getroot() if hasattr(doc, "getroot") else doc
            xml_version = root.get("version")
            if xml_version and self.xsd_version and xml_version != self.xsd_version:
                warnings.warn(
                    f"LibRML version mismatch: XML version is {xml_version}, "
                    f"but XSD version is {self.xsd_version}.",
                    UserWarning,
                )

            self.xsd.assertValid(doc)
            return True, None
        except etree.DocumentInvalid as e:
            return False, str(e)
        except Exception as e:
            return False, f"XML Parsing Error: {str(e)}"

    def validate_json(self, json_data: Union[dict, str, Path]) -> tuple[bool, Optional[str]]:
        try:
            if isinstance(json_data, Path):
                with open(json_data, "r") as f:
                    data = json.load(f)
            elif isinstance(json_data, str):
                data = json.loads(json_data)
            else:
                data = json_data

            validate_json_schema(instance=data, schema=self.json_schema)
            return True, None
        except JSONValidationError as e:
            return False, e.message
        except Exception as e:
            return False, f"JSON Error: {str(e)}"
