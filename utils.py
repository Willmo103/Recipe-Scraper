import json


def write_json(root_file_path: str, data: dict):
    file_name = data.get("name")
    with open(f"{root_file_path}/{file_name}.json", "w") as f:
        data = json.dump(data, f)
        print(f"{file_name}.json Successfully written!")
