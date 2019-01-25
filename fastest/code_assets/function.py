import ast
from fastest.code_assets.naive_case_detector import get_test_from_example_passage


def get_functions_from_node(node):
    """
    Extract functions from ast node
    :param node:
    :return: list
    """
    return [{
        'name': n.name,
        'tests': get_test_from_example_passage(ast.get_docstring(n))
    } for n in node.body if isinstance(n, ast.FunctionDef)]


def get_functions(page):
    """
    Read a python script and extract functions and class methods
    and add them to a list
    ------
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    page = TestBodies.GET_FUNCTIONS_TEST_CASE_1
    @end

    1) get_functions(page) -> TestBodies.GET_FUNCTIONS_TEST_CASE_1_EXPECT
    ------
    :param page: str
    :return: list
    """
    node = ast.parse(page)
    functions = get_functions_from_node(node)
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    methods = [get_functions_from_node(class_) for class_ in classes]
    return functions + methods
