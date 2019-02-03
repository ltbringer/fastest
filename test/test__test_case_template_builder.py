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
    def test__case_generator__88A2BECDDA(self):
        self.assertEqual(case_generator('a55eff11-ed51-ecb37-ccba'), 'A55EFF11ED')

class TestTestCaseTemplateBuilderGetEmptyOfType(unittest.TestCase):
    def test__get_empty_of_type__97BFE255AD(self):
        self.assertIsInstance(get_empty_of_type(''), str)
        self.assertEqual(get_empty_of_type('str'), "''")
    def test__get_empty_of_type__E829F5B2F3(self):
        self.assertIsInstance(get_empty_of_type(''), str)
        self.assertEqual(get_empty_of_type('???'), None)

class TestTestCaseTemplateBuilderGetParamsList(unittest.TestCase):
    def test__get_params_list__5896A6FF77(self):
        self.assertIsInstance(get_params_list([]), list)
        self.assertEqual(get_params_list(['str', 'str', 'list', 'dict']), ["''", "''", '[]', '{}'])
    def test__get_params_list__008552C2B7(self):
        self.assertIsInstance(get_params_list([]), list)
        self.assertEqual(get_params_list(['str', '???']), ["''"])

class TestTestCaseTemplateBuilderCreateTypeTestCase(unittest.TestCase):
    def test__create_type_test_case__15E734DB44(self):
        self.assertIsInstance(create_type_test_case({}, []), str)        
        function_object = {
            'tests': {
                'return': 'str'
            },
            'name': 'function_1'
        }
        params = ['str', 'str']
        

        self.assertEqual(create_type_test_case(function_object, params), TestBodies.TYPE_TEST_CASE_1)

class TestTestCaseTemplateBuilderCreateTypeTestCaseIfParams(unittest.TestCase):
    def test__create_type_test_case_if_params__724ADEA5F5(self):
        self.assertIsInstance(create_type_test_case_if_params({}, []), str)        
        function_object = {
            'tests': {
                'return': 'str'
            },
            'name': 'function_1'
        }
        
        params = ['str', 'str']
        

        self.assertEqual(create_type_test_case_if_params(function_object, params), TestBodies.TYPE_TEST_CASE_2)

class TestTestCaseTemplateBuilderIsTypeTestReady(unittest.TestCase):
    def test__is_type_test_ready__A9533190C0(self):
        self.assertIsInstance(is_type_test_ready({}, []), bool)        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_1, params), True)
    def test__is_type_test_ready__D7209799B8(self):
        self.assertIsInstance(is_type_test_ready({}, []), bool)        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_2, params), False)
    def test__is_type_test_ready__F77E0DF3C5(self):
        self.assertIsInstance(is_type_test_ready({}, []), bool)        
        function_object_1 = {
            'tests': {
                'return': 'str'
            }
        }
        
        function_object_2 = {'tests': {}}
        
        params = ['str', 'str']
        

        self.assertEqual(is_type_test_ready(function_object_1, []), False)

class TestTestCaseTemplateBuilderCreateAssertionTest(unittest.TestCase):
    def test__create_assertion_test__C943C950DB(self):
        self.assertIsInstance(create_assertion_test({}), str)        
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }
        
        function_object_2 = {'tests': {'variables': []}}
        
        params = ['str', 'str']
        

        self.assertEqual(create_assertion_test(function_object_1), TestBodies.ASSERTION_TEST_1)
    def test__create_assertion_test__35B47A9C25(self):
        self.assertIsInstance(create_assertion_test({}), str)        
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }
        
        function_object_2 = {'tests': {'variables': []}}
        
        params = ['str', 'str']
        

        self.assertEqual(create_assertion_test(function_object_2), '')

class TestTestCaseTemplateBuilderCreateNaiveTestCase(unittest.TestCase):
    def test__create_naive_test_case__F2F4E8B23C(self):
        self.assertIsInstance(create_naive_test_case({}, {}, ''), str)        
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
        
        exception_test = {
            'from': 'function_2(None)',
            'exception': 'TypeError'
        }
        
        test_id = 'a55eff11-ed51-ecb37-ccba'
        

        self.assertEqual(create_naive_test_case(function_object, test, test_id), TestBodies.NAIVE_TEST_RESULT)
    def test__create_naive_test_case__4E75A16719(self):
        self.assertIsInstance(create_naive_test_case({}, {}, ''), str)        
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
        
        exception_test = {
            'from': 'function_2(None)',
            'exception': 'TypeError'
        }
        
        test_id = 'a55eff11-ed51-ecb37-ccba'
        

        self.assertEqual(create_naive_test_case(function_object, exception_test, test_id), TestBodies.EXCEPTION_TEST_RESULT)
