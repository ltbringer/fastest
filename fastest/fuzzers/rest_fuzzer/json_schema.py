def type_name(item):
    """
    ----
    examples:

    1) type_name('apple') -> 'str'
    ----
    :param item:
    :return:
    """
    return type(item).__name__


def schema_fn(type_of_item):
    """
    ----
    examples:

    1) schema_fn("str") -> get_schema_for_primitive
    ----
    :param type_of_item:
    :return:
    """
    type_fn_list = {
        "str": get_schema_for_primitive,
        "int": get_schema_for_primitive,
        "float": get_schema_for_primitive,
        "list": get_schema_for_list,
        "dict": get_schema_for_dict
    }
    return type_fn_list[type_of_item]


def get_schema_for_primitive(name, type_of_item):
    """
    ----
    examples:

    1) get_schema_for_primitive('', '') -> []
    ----
    :param name:
    :param type_of_item:
    :return:
    """
    return []


def get_schema_for_list(body, type_of_item):
    """
    ----
    examples:

    @let
    schema_object = {
        'inner': [{
            'inner': [],
            'name': 'key',
            'type': 'int'
        }],
        'name': '__auto__',
        'type': 'dict'
    }
    @end

    1) get_schema_for_list([{"key": 1}], "list") -> schema_object
    ----
    :param body:
    :param type_of_item:
    :return:
    """
    element = body[0] if isinstance(body, list) and len(body) > 0 else None
    return {
        "name": "__auto__",
        "type": type_name(element),
        "inner": get_schema_for(element, type_name(element))
    }


def get_schema_for_dict(body, type_of_item):
    """
    ----
    examples:

    1) get_schema_for_dict({'key': 1}, 'dict') -> [{'type': 'int', 'inner': [], 'name': 'key'}]
    ----
    :param body:
    :param type_of_item:
    :return:
    """
    return [{
        "name": key,
        "type": type_name(body[key]),
        "inner": get_schema_for(body[key], type_name(body[key]))
    } for key in body.keys()]


def get_schema_for(item, type_of_item):
    """
    ----
    examples:

    1) get_schema_for({"key": 1}, 'dict') -> [{'type': 'int', 'inner': [], 'name': 'key'}]
    ----
    :param item:
    :param type_of_item:
    :return:
    """
    return schema_fn(type_of_item)(item, type_of_item)


def make_schema_object(req_body):
    """
    ----
    examples:

    @let
    schema_object = {
        'inner': [{'inner': [], 'name': 'key', 'type': 'int'}],
        'name': '__root__',
        'type': 'dict'
    }
    @end

    1) make_schema_object({"key": 1}) -> schema_object
    ----
    :param req_body:
    :return:
    """
    return {
        "name": "__root__",
        "type": type_name(req_body),
        "inner": get_schema_for(req_body, type_name(req_body))
    }
