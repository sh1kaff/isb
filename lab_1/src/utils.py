import json

def json_to_dict(path: str) -> dict:
    with open(path, "r", encoding="utf-8-sig") as file:
        settings = json.load(file)
        return settings

def read_settings() -> dict:
    return json_to_dict("config\\settings.json")


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

  