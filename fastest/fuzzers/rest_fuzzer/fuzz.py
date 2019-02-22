from fastest.fuzzers.primitive_fuzzer.fuzz import random_integers, random_ascii_chars, random_float


def build_empty_of_type(item_type):
    empty_values_for_types = {
        "str": random_ascii_chars,
        "int": random_integers,
        "float": random_float,
        "list": lambda: [],
        "dict": lambda: {}
    }
    return empty_values_for_types[item_type]


def schema_to_object_builder(schema, name='__root__'):
    root_object = build_empty_of_type(schema['type'])()

    if schema['type'] == 'list':
        root_object.append(schema_to_object_builder(schema['inner']))

    elif schema['type'] == 'dict':
        for prop in schema['inner']:
            root_object[prop['name']] = schema_to_object_builder(prop)

    return root_object
