import random
import requests
from fuzzer import random_integers, random_ascii_chars, random_float


def build_one_of_type(item_type, p=1.0):
    empty_values_for_types = {
        "str": random_ascii_chars,
        "int": random_integers,
        "float": random_float,
        "list": lambda: [],
        "dict": lambda: {},
        "null": lambda: None
    }
    basic_types = ['str', 'int', 'float', 'list', 'dict', 'null']
    mutation = random.random()
    return empty_values_for_types[item_type] \
        if p > mutation \
        else empty_values_for_types[random.choice(basic_types)]


def schema_to_object_builder(schema, p=1.0):
    mutation = random.random()
    type_of_object = schema['type'] if isinstance(schema, dict) else "null"
    root_object = build_one_of_type(type_of_object, p)()

    if isinstance(root_object, list):
        if p > mutation:
            root_object.append(schema_to_object_builder(schema['inner'], p=mutation))

    elif isinstance(root_object, dict):
        for prop in schema['inner']:
            if p > mutation:
                root_object[prop['name']] = schema_to_object_builder(prop, p=mutation)

    return root_object


def rules(host, port, api_list):
    """
    api_list = [{
        "url": "/some/path",
        "method": "POST",
        "body": {}
    }]
    """

    for api in api_list:
        requests.request(
            method=api['method'],
            url='{host}:{port}{url}'.format(host=host, port=port, url=api['url'])
        )

    return {}
