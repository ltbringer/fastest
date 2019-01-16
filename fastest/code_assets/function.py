import ast
from fastest.code_assets.arguments import get_args
from fastest.code_assets.variables import get_variables
from fastest.code_assets.return_value import get_return_values
from fastest.code_assets.naive_case_detector import get_test_from_example_passage



def get_functions_from_node(node):
    return [{
        'name': n.name,
        'tests': get_test_from_example_passage(ast.get_docstring(n))
    } for n in node.body if isinstance(n, ast.FunctionDef)]


def get_functions(page):
    """

    :param page:
    :return:
    """
    node = ast.parse(page)
    functions = get_functions_from_node(node)
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    methods = [get_functions_from_node(class_) for class_ in classes]
    return functions + methods
