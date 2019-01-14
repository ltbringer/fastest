CURRENT_DEPTH_THRESHOLD = 20


def is_function_too_long(function_body):
    """
    example: is_function_too_long("\n\n\n\n\n") -> (False, 6)#
    example: is_function_too_long("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") -> (True, 31) #
    :param function_body:
    :return:
    """
    naive_code_depth = len(function_body.split('\n'))
    return naive_code_depth >= CURRENT_DEPTH_THRESHOLD, naive_code_depth
