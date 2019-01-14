import re
from fastest.code_assets.arguments import get_args
from fastest.code_assets.variables import get_variables
from fastest.code_assets.return_value import get_return_values
from fastest.code_assets.naive_case_detector import get_naive_case


def get_functions(page):
    """
    example: get_functions("def fn(arg1, arg2):\narg1 += 1\n\treturn arg1 + arg2") -> [{
        'name': 'fn',
        'args': ['arg1', 'arg2'],
        'str': 'def fn(arg1, arg2):\n\treturn arg1 + arg2',
        'vars': [],
        'tests': []
    }]
    #
    :param page:
    :return:
    """
    statements = re.split(r'\n', page)
    function_map = []
    function_finder = None
    function_running = False
    function_object = {}
    function_body_start = 0
    for statement_number, _ in enumerate(statements):
        if function_running is False:
            function_finder = re.match(r'def ((\w[A-Za-z_]*[^\(])(\(.*[^:]\)))', statements[statement_number])
            function_body_start = statement_number

        if function_finder is not None:
            function_running = True
            function_object['name'] = function_finder.group(2)
            function_object['args'] = get_args(function_finder.group(3))
            function_finder = None

        if function_body_start != statement_number and re.match(r'^\s+', statements[statement_number]) is None:
            function_object['str'] = '\n'.join(statements[function_body_start: statement_number])
            function_object['returns'] = get_return_values(function_object['str'])
            function_object['vars'] = get_variables(function_object['str'], function_object['args'])
            function_object['tests'] = get_naive_case(function_object['str'])
            function_map.append(function_object)
            function_object = {}
            function_running = False
            function_finder = None


    return function_map
