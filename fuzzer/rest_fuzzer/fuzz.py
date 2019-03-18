import random
import requests
from fuzzer.primitive_fuzzer.fuzz import random_integers, random_ascii_chars, random_float


MUTATION_LIMIT = 0.1


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
    return empty_values_for_types[item_type] \
        if MUTATION_LIMIT < p \
        else empty_values_for_types[random.choice(basic_types)]


def schema_to_object_builder(schema_obj, p=1.0):
    mutations, schema = schema_obj
    mutation = mutations if isinstance(mutations, float) else mutations[0]

    type_of_object = schema['type'] if isinstance(schema, dict) else "null"
    root_object = build_one_of_type(type_of_object, p)()

    if not isinstance(schema, dict):
        return root_object

    if isinstance(root_object, list):
        root_object.append(schema_to_object_builder(
            schema.get('inner', {}),
            p=schema.get('inner', {})[0]
        ))

    elif isinstance(root_object, dict):
        for prop in schema['inner'][1]:
            root_object[prop['name']] = schema_to_object_builder((schema['inner'][0], prop), p=mutation)

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
        request_body = schema_to_object_builder(body_schema)
        return request_body, requests.request(
            method=api_object['method'],
            url=url,
            json=request_body
        )

    elif api_object['method'] in ['GET', 'DELETE']:
        return None, requests.request(
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
            request_body, r = api(host, port, api_object, body_schema)
            f.write(
                "url: {}\nrequest_body: {}\nresponse: {}\nstatus_code: {}\n\n".format(
                    api_object['url'], request_body,  r.text, r.status_code
                )
            )
