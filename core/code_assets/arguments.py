def get_args(args_str):
    args_str = args_str.strip()
    args_str = args_str.replace('(', '')
    args_str = args_str.replace(')', '')
    args = args_str.split(',')
    args = [arg.strip() for arg in args]
    return args