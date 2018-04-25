import json

default_sort_keys = True
default_indent = 4


def print_json(obj: object):
    print(string_json(obj))


def string_json(obj: object, sort: bool=default_sort_keys, indents: int=default_indent):
    if type(obj) is str:
        return json.dumps(json.loads(obj), sort_keys=sort, indent=indents)
    else:
        return json.dumps(obj, sort_keys=sort, indent=indents)
