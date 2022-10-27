import json


def write_json(root_file_path: str, data: dict):
    with open(f"{root_file_path}/{data.get('name')}.json", "w") as f:
        data = json.dump(data, f)
