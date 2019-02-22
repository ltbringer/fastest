import random
from fastest.fuzzers.primitive_fuzzer.fuzz import random_integers, random_ascii_chars, random_float


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
    root_object = build_one_of_type(schema['type'])()

    if isinstance(root_object, list):
        if p > mutation:
            root_object.append(schema_to_object_builder(schema['inner'], p=p))

    elif isinstance(root_object, dict):
        for prop in schema['inner']:
            if p > mutation:
                root_object[prop['name']] = schema_to_object_builder(prop, p=p)

    return root_object
