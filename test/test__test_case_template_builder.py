from fastest.bodies.test_case_template_builder import case_generator
from fastest.bodies.test_case_template_builder import create_assertion_test
from fastest.bodies.test_case_template_builder import create_naive_test_case
from fastest.bodies.test_case_template_builder import get_empty_of_type
from fastest.bodies.test_case_template_builder import get_params_list
from fastest.constants import TestBodies
import unittest


class TestTestCaseTemplateBuilderCaseGenerator(unittest.TestCase):
    def test__case_generator__8225DC6932(self):
        self.assertEqual(case_generator('a55eff11-ed51-ecb37-ccba'), 'A55EFF11ED')


class TestTestCaseTemplateBuilderGetEmptyOfType(unittest.TestCase):
    def test__get_empty_of_type__172C024CCA(self):
        self.assertEqual(get_empty_of_type('str'), "''")

    def test__get_empty_of_type__D2E8A93D65(self):
        self.assertEqual(get_empty_of_type('???'), None)


class TestTestCaseTemplateBuilderGetParamsList(unittest.TestCase):
    def test__get_params_list__89DBCF6E3F(self):
        self.assertEqual(get_params_list(['str', 'str', 'list', 'dict']), ["''", "''", '[]', '{}'])

    def test__get_params_list__AAF390360D(self):
        self.assertEqual(get_params_list(['str', '???']), ["''"])


class TestTestCaseTemplateBuilderCreateAssertionTest(unittest.TestCase):
    def test__create_assertion_test__CB2DD2E947(self):
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }

        self.assertEqual(create_assertion_test(function_object_1), TestBodies.ASSERTION_TEST_1)

    def test__create_assertion_test__B2EEBEFE46(self):
        function_object_2 = {'tests': {'variables': []}}

        self.assertEqual(create_assertion_test(function_object_2), '')


class TestTestCaseTemplateBuilderCreateNaiveTestCase(unittest.TestCase):
    def test__create_naive_test_case__42FE31258A(self):
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

    def test__create_naive_test_case__2A4AD614E0(self):
        function_object = {
            'tests': {
                'return': 'str',
                'variables': ['a = 5']
            },
            'name': 'function_1'
        }

        exception_test = {
            'from': 'function_2(None)',
            'exception': 'TypeError'
        }

        test_id = 'a55eff11-ed51-ecb37-ccba'

        self.assertEqual(create_naive_test_case(function_object, exception_test, test_id),
                         TestBodies.EXCEPTION_TEST_RESULT)
