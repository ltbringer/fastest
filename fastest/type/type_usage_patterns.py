import re
from fastest.utils import count_truthy


def used_as_int(statement, variable):
    """
    example: used_as_int("a = 4", "a") -> 1 #
    example: used_as_int("a + 4", "a") -> 1 #
    example: used_as_int("a * 4", "a") -> 1 #
    example: used_as_int("a - 4", "a") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement       = statement.strip()
    assignment      = re.search(r'{variable}\s*=\s*\d+'.format(variable=variable), statement)
    addition        = re.search(r'{variable}\s*\+\s*'.format(variable=variable), statement)
    addition_inc    = re.search(r'{variable}\s*\+=\s*\d+'.format(variable=variable), statement)
    multiplication  = re.search(r'{variable}\s*\*\s*'.format(variable=variable), statement)
    subtraction     = re.search(r'{variable}\s*-\s*'.format(variable=variable), statement)
    division        = re.search(r'{variable}\s*/\s*'.format(variable=variable), statement)
    return count_truthy([assignment, addition, subtraction,multiplication, division, addition_inc])

def used_as_str(statement, variable):
    """
    example: used_as_str("string_var = 'something'", "string_var") -> 1 #
    example: used_as_str("string_var + 'something'", "string_var") -> 1 #
    example: used_as_str("string_var * 5", "string_var") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement       = statement.strip()
    assignment      = re.match('{variable}\s*=\s*"|\'\w*"|\''.format(variable=variable), statement)
    addition        = re.match(r'{variable}\s*\+\s*'.format(variable=variable), statement)
    multiplication  = re.match(r'{variable}\s*\*\d*'.format(variable=variable), statement)
    return count_truthy([assignment, addition, multiplication])


def used_as_iterable(statement, variable):
    """
    example: used_as_iterable("for word in words", "words") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement               = statement.strip()
    loop                    = re.match(r'for \w+ in {variable}'.format(variable=variable), statement)
    map_fn                  = re.search(r'map\(.*[^,)],\s*{variable}'.format(variable=variable), statement)
    filter_fn               = re.search(r'filter\(.*[^,)],\s*{variable}'.format(variable=variable), statement)
    reduce_fn               = re.search(r'reduce\(.*[^,)],\s*{variable}'.format(variable=variable), statement)
    item_index              = re.match(r'{variable}\[\d+\]'.format(variable=variable), statement)
    return count_truthy([loop, map_fn, filter_fn, reduce_fn, item_index])


def used_as_list(statement, variable):
    """
    example: used_as_list("apples.append(10)", "apples") -> 1 #
    example: used_as_list("apples = [11, 12]", "apples") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement               = statement.strip()
    assignment              = re.match(r'{variable}\s*=\s*\['.format(variable=variable), statement)
    assignment_as_instance  = re.match(r'{variable}\s*=\s*list\('.format(variable=variable), statement)
    append                  = re.search(r'{variable}.append\('.format(variable=variable), statement)
    return count_truthy([assignment_as_instance, assignment, append]) + used_as_iterable(statement, variable)


def used_as_tuple(statement, variable):
    """
    example: used_as_tuple("words = (11, 2)", "words") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement               = statement.strip()
    assignment              = re.match(r'{variable}\s*=\s*\('.format(variable=variable), statement)
    assignment_as_instance  = re.match(r'{variable}\s*=\s*tuple\('.format(variable=variable), statement)
    insert                  = re.match(r'{variable}.insert\('.format(variable=variable), statement)
    return count_truthy([assignment_as_instance, assignment, insert]) + used_as_iterable(statement, variable)


def used_as_dict(statement, variable):
    """
    example: used_as_dict("dict_input['val']", "dict_input") -> 1 #
    :param statement:
    :param variable:
    :return:
    """
    statement       = statement.strip()
    assignment      = re.search(r'{variable}\s*=\s*\{{'.format(variable=variable), statement)
    key_ref_str     = re.search(r'{variable}\[\"|\'\w+\"|\'\]'.format(variable=variable), statement)
    key_ref_var     = re.search(r'{variable}\[\w+\]'.format(variable=variable), statement)
    get_access      = re.search(r'{variable}.get\('.format(variable=variable), statement)
    return count_truthy([assignment, key_ref_str, key_ref_var, get_access])
