from fastest.code_assets.function import get_functions
from fastest.constants import TestBodies
import unittest


class TestFunctionGetFunctions(unittest.TestCase):
    def test__get_functions__A46AF6E43F(self):
        self.assertIsInstance(get_functions(''), list)
        page = TestBodies.GET_FUNCTIONS_TEST_CASE_1
        self.assertEqual(get_functions(page), TestBodies.GET_FUNCTIONS_TEST_CASE_1_EXPECT)

    def test__get_functions__5C1F8B243A(self):
        self.assertIsInstance(get_functions(''), list)
        page_with_syntax_error = TestBodies.PAGE_WITH_SYNTAX_ERRORS
        self.assertEqual(get_functions(page_with_syntax_error), [])
