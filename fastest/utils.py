def count_truthy(items):
    """
    Count non None values viz, but includes 0
    ----
    examples:

    1) count_truthy([1, 2, None, 'a']) -> 3
    2) count_truthy([1, 2, 0, 'a']) -> 4
    ----
    :param items: list
    :return: int
    """
    counter = 0
    for item in items:
        if item is not None:
            counter += 1
    return counter


def to_camel_case(snake_str):
    """
    Convert snake case to CamelCase
    -----
    examples:

    1) to_camel_case('snake_cased_string') -> 'SnakeCasedString'
    -----
    :param snake_str: str
    :return: str
    """
    components = snake_str.split('_')
    return components[0].title() + ''.join(x.title() for x in components[1:])
