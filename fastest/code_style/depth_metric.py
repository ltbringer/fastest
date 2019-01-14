CURRENT_DEPTH_THRESHOLD = 20


def is_function_too_long(function_body):
    naive_code_depth = len(function_body.split('\n'))
    return naive_code_depth >= CURRENT_DEPTH_THRESHOLD, naive_code_depth
