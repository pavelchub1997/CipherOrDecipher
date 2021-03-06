import json
import os
import pathlib
import string
import functools

GET_ABSOLUTE_PATH_FOR_JSON_FILE = pathlib.Path(os.path.abspath(__file__)).parent.resolve()


def get_data_from_json(file_json: str):
    with open(
            os.path.join(GET_ABSOLUTE_PATH_FOR_JSON_FILE, "../config", file_json),
            encoding='utf-8',
            errors='ignore'
    ) as json_data:
        data = json.load(json_data, strict=False)
    return data


def write_data_to_file(name_file: str, data: str):
    with open(name_file, "w") as result_file:
        result_file.write(data)


def generate_alphabet(config: dict):
    return [chr(index) for index in range(config["start"], config["stop"])] + \
           [letter for letter in string.printable][:-6]
