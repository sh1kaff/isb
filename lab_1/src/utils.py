import json
import os


def json_to_dict(path: str) -> dict:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Invalid path to file: '{path}'")

    if not path.endswith(".json"):
        raise ValueError(f"The file '{path}' is not a json file")

    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            return settings
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f"Json file '{path}' is invalid")


def read_settings() -> dict:
    settings_path = os.path.join(os.path.dirname(__file__), "..", "config", "settings.json")
    return json_to_dict(settings_path)


def write_to_file(path: str, text: str):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Invalid path to file: '{path}'")
    
    with open(path, "w", encoding="utf-8-sig") as file:
        file.write(text)


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Invalid path to file: '{path}'")

    with open(path, "r", encoding="utf-8-sig") as file:
        return file.read()


if __name__ == "__main__":
    json_to_dict(R"C:\Users\user\Desktop\UNIVERSITY\isb\lab_1\src\parsing.py")
