def detect_type_check(statements, argument):
    """
    example: detect_type_check(["if type(var) is str"], "var") -> True #
    example: detect_type_check(["if True"], "var") -> False #
    :param statements:
    :param argument:
    :return:
    """
    for statement in statements:
        # TODO: Does not scale need patterns for string
        if 'if type({argument})'.format(argument=argument) in statement:
            return True
    return False
