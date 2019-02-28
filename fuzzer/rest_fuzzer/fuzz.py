import random
import requests
from fuzzer.primitive_fuzzer.fuzz import random_integers, random_ascii_chars, random_float


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

    if isinstance(root_object, list) and isinstance(schema, dict) and p > mutation:
            root_object.append(schema_to_object_builder(schema['inner'], p=mutation))

    elif isinstance(root_object, dict) and isinstance(schema, dict):
        for prop in schema['inner']:
            if p > mutation:
                root_object[prop['name']] = schema_to_object_builder(prop, p=mutation)

    return root_object


def api(host, port, api_object, body_schema):
    """
    api_object = {
        "url": "/some/path",
        "method": "POST",
        "tests": 100,
        "body": {}
    }
    """
    url = '{host}:{port}{url}'.format(host=host, port=port, url=api_object['url'])

    if api_object['method'] in ['POST', 'PUT', 'PATCH']:
        return requests.request(
            method=api_object['method'],
            url=url,
            json=schema_to_object_builder(body_schema)
        )

    elif api_object['method'] in ['GET', 'DELETE']:
        return requests.request(
            method=api_object['method'],
            url=url
        )


def api_nx(req_spec):
    host = req_spec.get('host')
    port = req_spec.get('port')
    api_object = req_spec.get('req_body')
    body_schema = req_spec.get('req_body_schema')
    tests = api_object.get('tests', 1000)

    for _ in range(tests):
        with open('fuzz.log', 'a+') as f:
            r = api(host, port, api_object, body_schema)
            f.write(
                "url: {}\nresponse: {}\nstatus_code: {}\n\n".format(
                    api_object['url'], r.text, r.status_code
                )
            )
