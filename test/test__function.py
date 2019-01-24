from fastest.code_assets.function import get_functions
from fastest.constants import TestBodies
import unittest

class TestFunctionGetFunctions(unittest.TestCase):
    def test__get_functions__7D85F3E67A(self):        
        page = TestBodies.GET_FUNCTIONS_TEST_CASE_1
        

        self.assertEqual(get_functions(page), TestBodies.GET_FUNCTIONS_TEST_CASE_1_EXPECT)
