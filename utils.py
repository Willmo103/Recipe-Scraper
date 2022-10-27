import json
import re


def write_json(root_file_path: str, data: dict) -> None:
    file_name = data.get("name")
    with open(f"{root_file_path}/{file_name}.json", "w") as f:
        data = json.dump(data, f)
        print(f"{file_name}.json Successfully written!")


def remove_blank_lines(str: str) -> str:
    lines = str.split("\n")
    non_empty = [line for line in lines if line.strip() != ""]

    strings = ""
    for line in non_empty:
        strings += line + "\n"
    return strings


def list_from_str(str: str) -> list:
    output = []
    lines = str.split("\n")
    for line in lines:
        if not line.startswith("For"):
            output.append(line.strip())
    return output
