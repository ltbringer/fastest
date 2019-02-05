from fastest.bodies.test_case_template_builder import case_generator
from fastest.bodies.test_case_template_builder import create_assertion_test
from fastest.bodies.test_case_template_builder import create_naive_test_case
from fastest.bodies.test_case_template_builder import get_empty_of_type
from fastest.bodies.test_case_template_builder import get_params_list

from fastest.constants import TestBodies
import unittest


class TestFCaseGenerator(unittest.TestCase):
    def test__case_generator__FEB45420EC(self):
        self.assertEqual(case_generator('a55eff11-ed51-ecb37-ccba'), 'A55EFF11ED')


class TestFGetEmptyOfType(unittest.TestCase):
    def test__get_empty_of_type__6AE4237E62(self):
        self.assertEqual(get_empty_of_type('str'), "''")

    def test__get_empty_of_type__F2B045FFA3(self):
        self.assertEqual(get_empty_of_type('???'), None)


class TestFGetParamsList(unittest.TestCase):
    def test__get_params_list__B1348ED47E(self):
        self.assertEqual(get_params_list(['str', 'str', 'list', 'dict']), ["''", "''", '[]', '{}'])

    def test__get_params_list__B2F225C40B(self):
        self.assertEqual(get_params_list(['str', '???']), ["''"])


class TestFCreateAssertionTest(unittest.TestCase):
    def test__create_assertion_test__ACB551FFCF(self):
        function_object_1 = {
            'tests': {
                'variables': ['a = 5']
            }
        }

        self.assertEqual(create_assertion_test(function_object_1), TestBodies.ASSERTION_TEST_1)

    def test__create_assertion_test__AE86DA16B8(self):
        function_object_2 = {'tests': {'variables': []}}

        self.assertEqual(create_assertion_test(function_object_2), '')


class TestFCreateNaiveTestCase(unittest.TestCase):
    def test__create_naive_test_case__D5CE6058D6(self):
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
