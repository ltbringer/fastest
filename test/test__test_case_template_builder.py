from fastest.bodies.test_case_template_builder import case_generator
from fastest.bodies.test_case_template_builder import create_assertion_test
from fastest.bodies.test_case_template_builder import create_naive_test_case
from fastest.bodies.test_case_template_builder import create_type_test_case
from fastest.bodies.test_case_template_builder import create_type_test_case_if_params
from fastest.bodies.test_case_template_builder import get_empty_of_type
from fastest.bodies.test_case_template_builder import get_params_list
from fastest.bodies.test_case_template_builder import is_type_test_ready
from fastest.constants import TestBodies
import unittest

class TestTestCaseTemplateBuilderCaseGenerator(unittest.TestCase):
    def test__case_generator__72ADA0717A(self):
        self.assertEqual(case_generator('a55eff11-ed51-ecb37-ccba'), 'A55EFF11ED')

class TestTestCaseTemplateBuilderGetEmptyOfType(unittest.TestCase):
    def test__get_empty_of_type__9EB02075E4(self):
        self.assertEqual(get_empty_of_type('str'), "''")
    def test__get_empty_of_type__9B37BF7153(self):
        self.assertEqual(get_empty_of_type('???'), None)

class TestTestCaseTemplateBuilderGetParamsList(unittest.TestCase):
    def test__get_params_list__57DA4784AF(self):
        self.assertEqual(get_params_list(['str', 'str', 'list', 'dict']), ["''", "''", '[]', '{}'])
    def test__get_params_list__3221AE3ADE(self):
        self.assertEqual(get_params_list(['str', '???']), ["''"])

class TestTestCaseTemplateBuilderCreateTypeTestCase(unittest.TestCase):
    def test__create_type_test_case__B9C103DF1B(self):        
        function_object = {
            'tests': {
                'return': 'str'
            },
            'name': 'function_1'
        }
        
        params = ['str', 'str']
        

        self.assertEqual(create_type_test_case(function_object, params), TestBodies.TYPE_TEST_CASE_1)

class TestTestCaseTemplateBuilderCreateTypeTestCaseIfParams(unittest.TestCase):
    def test__create_type_test_case_if_params__772EAEC008(self):        
        function_object = {
            'tests': {
                'return': 'str'
            },
            'name': 'function_1'
        }
        
        params = ['str', 'str']
        

        self.assertEqual(create_type_test_case_if_params(function_object, params), TestBodies.TYPE_TEST_CASE_2)

class TestTestCaseTemplateBuilderIsTypeTestReady(unittest.TestCase):
    def test__is_type_test_ready__415EA1D907(self):        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_1, params), True)
    def test__is_type_test_ready__91E5C34C00(self):        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_2, params), False)
    def test__is_type_test_ready__0117E5B237(self):        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_1, []), False)

class TestTestCaseTemplateBuilderCreateAssertionTest(unittest.TestCase):
    def test__create_assertion_test__2D20F4EA49(self):        
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }
        
        function_object_2 = {'tests': {'variables': []}}
        
        params = ['str', 'str']
        

        self.assertEqual(create_assertion_test(function_object_1), TestBodies.ASSERTION_TEST_1)
    def test__create_assertion_test__4ACD8132A4(self):        
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }
        
        function_object_2 = {'tests': {'variables': []}}
        
        params = ['str', 'str']
        

        self.assertEqual(create_assertion_test(function_object_2), '')

class TestTestCaseTemplateBuilderCreateNaiveTestCase(unittest.TestCase):
    def test__create_naive_test_case__64882A9F1F(self):        
        function_object = {
            'tests': {
                'return': 'str',
                'variables': ['a = 5']
            },
            'name': 'function_1'
        }
        
        test = {
            'from': 'function_1',
            'expect': '2'
        }
        
        test_id = 'a55eff11-ed51-ecb37-ccba'
        

        self.assertEqual(create_naive_test_case(function_object, test, test_id), TestBodies.NAIVE_TEST_RESULT)
