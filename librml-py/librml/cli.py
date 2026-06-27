import argparse
import json
import sys
from pathlib import Path

from librml.converter import json_to_xml, xml_to_json
from librml.validator import LibRMLValidator


def main():
    parser = argparse.ArgumentParser(description="LibRML Validator and Converter")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate a LibRML file")
    validate_parser.add_argument(
        "file", type=Path, help="Path to the file (XML or JSON)"
    )

    # Convert command
    convert_parser = subparsers.add_parser(
        "convert", help="Convert between XML and JSON"
    )
    convert_parser.add_argument("file", type=Path, help="Path to the input file")
    convert_parser.add_argument(
        "--to",
        choices=["xml", "json"],
        help="Target format (optional, inferred if not provided)",
    )
    convert_parser.add_argument("-o", "--output", type=Path, help="Output file path")

    args = parser.parse_args()

    if args.command == "validate":
        validator = LibRMLValidator()
        suffix = args.file.suffix.lower()

        if suffix == ".xml":
            valid, error = validator.validate_xml(args.file)
        elif suffix == ".json":
            valid, error = validator.validate_json(args.file)
        else:
            print(f"Unsupported file extension: {suffix}", file=sys.stderr)
            sys.exit(1)

        if valid:
            print(f"File {args.file} is valid.")
        else:
            print(f"File {args.file} is invalid: {error}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "convert":
        suffix = args.file.suffix.lower()
        target_format = args.to

        if not target_format:
            if suffix == ".xml":
                target_format = "json"
            elif suffix == ".json":
                target_format = "xml"
            else:
                print(
                    "Could not infer target format. Please use --to.", file=sys.stderr
                )
                sys.exit(1)

        if target_format == "json":
            with open(args.file, "rb") as f:
                content = f.read()
            result = xml_to_json(content)
            output_str = json.dumps(result, indent=2)
        else:
            if suffix == ".json":
                with open(args.file, "r") as f:
                    data = json.load(f)
            else:
                # Assuming XML input but converting to XML (maybe for formatting?)
                # Actually, the logic should be: if it's already XML, maybe just re-format?
                # But let's assume we convert from JSON to XML or re-format XML.
                # If target is XML and input is XML, let's just parse and re-emit.
                if suffix == ".xml":
                    with open(args.file, "rb") as f:
                        data = xml_to_json(f.read())
                else:
                    print(
                        f"Unsupported input for XML conversion: {suffix}",
                        file=sys.stderr,
                    )
                    sys.exit(1)

            output_bytes = json_to_xml(data)
            output_str = output_bytes.decode("utf-8")

        if args.output:
            with open(args.output, "w") as f:
                f.write(output_str)
        else:
            print(output_str)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
