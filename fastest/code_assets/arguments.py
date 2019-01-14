def get_args(args_str):
    """
    example: get_args(' (arg1, arg2) ') -> ['arg1', 'arg2'] #
    example: get_args('(arg1, arg2)') -> ['arg1', 'arg2'] #
    :param args_str:
    :return:
    """
    args_str = args_str.strip()
    args_str = args_str.replace('(', '')
    args_str = args_str.replace(')', '')
    args = args_str.split(',')
    args = [arg.strip() for arg in args]
    return args
