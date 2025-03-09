import json
import os

from config.messages import ERRORS

def write_to_file(path: str, text: str) -> None:
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))
    
    with open(path, "w", encoding="utf-8-sig") as file:
        file.write(text)


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))

    with open(path, "r", encoding="utf-8-sig") as file:
        return file.read()


def json_to_dict(path: str) -> dict:
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))

    if not path.endswith(".json"):
        raise ValueError(ERRORS["file_not_json"].format(path=path))

    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            return settings
    except json.decoder.JSONDecodeError as e:
        raise ValueError(ERRORS["invalid_json"].format(path=path, e=e))


def read_settings() -> dict:
    settings_path = os.path.join(os.path.dirname(__file__), "..", "config", "settings.json")
    return json_to_dict(settings_path)


def get_frequency(lang: str) -> dict:
    settings = read_settings().get("letter_frequency", {})
    path = settings.get(lang, "")

    return json_to_dict(path)