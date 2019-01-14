import re


def get_return_values(statements):
    """
    example: get_return_values('return 5') -> ['5'] #
    example: get_return_values('') -> [None] #
    :param statements:
    :return:
    """
    return_values = re.findall(r'return (.*)', statements)
    if len(return_values) > 0:
        return return_values
    else:
        return [None]
