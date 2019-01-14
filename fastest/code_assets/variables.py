import re
from fastest.code_assets import keywords


def get_variables(statements, arguments):
    """
    example: get_variables("def fn(arg1, arg2):\n\tc = 4\n\treturn arg1 + arg2", ["arg1", "arg2"]) -> ["c"] #
    :param statements:
    :param arguments:
    :return:
    """
    statements = statements.split('\n')
    statements = statements[1:]
    statements = ' '.join(statements)
    statements = re.sub(r'\s+', ' ', statements).replace(':', '')
    words = statements.split(' ')
    exclude_options = keywords.RESERVED + arguments
    return list(set([word for word in words if word not in exclude_options and word.isalpha()]))
