import subprocess
import sys
from pathlib import Path


def run_cli(*args):
    # Ensure librml-py is in PYTHONPATH
    env = {"PYTHONPATH": str(Path(__file__).parent.parent)}
    result = subprocess.run(
        [sys.executable, "-m", "librml"] + list(args),
        capture_output=True,
        text=True,
        env=env,
    )
    return result


def test_cli_validate_xml(tmp_path):
    xml_file = tmp_path / "test.xml"
    xml_file.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<libRML version="0.5.0" xmlns="http://librml.org/schema">
  <item id="test-cli"/>
</libRML>
""")
    # Need to make sure validator can find schemas when run via CLI
    # The validator uses Path(__file__).parent / "schemas"
    # When run as -m librml, it should work.

    result = run_cli("validate", str(xml_file))
    assert result.returncode == 0
    assert "is valid" in result.stdout


def test_cli_convert_xml_to_json(tmp_path):
    xml_file = tmp_path / "test.xml"
    xml_file.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<libRML version="0.5.0" xmlns="http://librml.org/schema">
  <item id="test-cli-conv"/>
</libRML>
""")
    result = run_cli("convert", str(xml_file))
    assert result.returncode == 0
    assert '"id": "test-cli-conv"' in result.stdout


def test_cli_convert_json_to_xml(tmp_path):
    json_file = tmp_path / "test.json"
    json_file.write_text('{"id": "test-json-cli"}')

    result = run_cli("convert", str(json_file))
    assert result.returncode == 0
    assert 'id="test-json-cli"' in result.stdout
