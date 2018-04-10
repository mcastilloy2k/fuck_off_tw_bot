import json


def read_file(filename: str):
    with open(filename) as f:
        return json.loads(f.read())
