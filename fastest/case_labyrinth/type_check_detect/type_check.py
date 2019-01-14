def detect_type_check(statements, argument):
    for statement in statements:
        # TODO: Does not scale need patterns for string
        if 'if type({argument})'.format(argument=argument) in statement:
            return True
    return False
