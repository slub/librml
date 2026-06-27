# LibRML Python Validator and Converter

A Python module and CLI tool to validate LibRML files and convert between XML and JSON representations.

## Features

- Validate LibRML XML files against XSD.
- Validate LibRML JSON files against JSON Schema.
- Bidirectional conversion between XML and JSON.
- Command-line interface for easy use.

## Installation

```bash
pip install .
```

## Usage

### CLI

```bash
# Validate
librml validate path/to/file.xml
librml validate path/to/file.json

# Convert
librml convert path/to/file.xml -o path/to/file.json
librml convert path/to/file.json -o path/to/file.xml
```

### Module

```python
from librml import LibRMLValidator, xml_to_json, json_to_xml

# Validation
validator = LibRMLValidator()
is_valid, error = validator.validate_xml(xml_bytes)

# Conversion
json_data = xml_to_json(xml_bytes)
xml_bytes = json_to_xml(json_data)
```
