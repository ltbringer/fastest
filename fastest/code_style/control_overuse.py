import re


CURRENT_CONDITIONAL_THRESHOLD = 5
CURRENT_CONTROL_COMPLEXITY_THRESHOLD = 3


def has_too_many_if_statements(function_body):
    """
    example: has_too_many_if_statements("if \nif \nif \nif \nif \nif \nif ") -> (True, 7) #
    example: has_too_many_if_statements("if if if") -> (False, 3) #
    :param function_body:
    :return:
    """
    matches = re.findall(r'if|elif|else', function_body)
    return len(matches) >= CURRENT_CONDITIONAL_THRESHOLD, len(matches)


def get_indent_of_loop(statement):
    """
    example: get_indent_of_loop("   for i in range(10):") -> 3 #
    :param statement:
    :return:
    """
    return len(re.findall(r'\s+?(?=for)', statement)[0])


def get_statements_from_function_body(function_body):
    """
    example: get_statements_from_function_body("a\n b") -> ['a', ' b'] #
    :param function_body:
    :return:
    """
    return [
        statement for statement
        in function_body.split('\n')
        if len(statement.strip()) > 0
    ]


def count_loop_indents(function_body):
    """
    example: count_loop_indents("   for i in range(1):") -> [3] #
    :param function_body:
    :return:
    """
    statements = get_statements_from_function_body(function_body)
    loops = []

    for statement in statements:
        if re.match(r'for ', statement.strip()):
            loops.append(get_indent_of_loop(statement))

    return loops


def get_loop_complexity(function_body):
    """
    example: get_loop_complexity("   for i in range(1):\n       for i in range(1):") -> (False, 1) #
    :param function_body:
    :return:
    """
    loop_indents = count_loop_indents(function_body)
    complexity = 0
    for i, _ in enumerate(loop_indents):
        if len(loop_indents) > i + 1 and loop_indents[i] < loop_indents[i + 1]:
            complexity += 1
    return CURRENT_CONTROL_COMPLEXITY_THRESHOLD < complexity, complexity
