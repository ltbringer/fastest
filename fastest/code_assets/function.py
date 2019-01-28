import ast
from fastest.code_assets.naive_case_detector import get_test_from_example_passage
from fastest.logger.logger import logger


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
    page_with_syntax_error = TestBodies.PAGE_WITH_SYNTAX_ERRORS
    @end

    1) get_functions(page) -> TestBodies.GET_FUNCTIONS_TEST_CASE_1_EXPECT
    2) get_functions(page_with_syntax_error) -> []
    ------
    :param page: str
    :return: list
    """
    try:
        node = ast.parse(page)
        functions = get_functions_from_node(node)
        classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
        methods = [get_functions_from_node(class_) for class_ in classes]
        return functions + methods
    except SyntaxError as error:
        logger.error(error)
        return []

