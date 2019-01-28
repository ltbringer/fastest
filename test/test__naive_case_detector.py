from fastest.code_assets.naive_case_detector import format_imports
from fastest.code_assets.naive_case_detector import get_imports_from_docstring
from fastest.code_assets.naive_case_detector import get_params_from_docstring
from fastest.code_assets.naive_case_detector import get_return_from_docstring
from fastest.code_assets.naive_case_detector import get_test_case_examples
from fastest.code_assets.naive_case_detector import get_test_from_example_passage
from fastest.code_assets.naive_case_detector import get_variables_from_docstring
from fastest.code_assets.naive_case_detector import stack_examples
from fastest.constants import TestBodies
import unittest


class TestNaiveCaseDetectorFormatImports(unittest.TestCase):
    def test__format_imports__2D5BFFE1F4(self):
        self.assertIsInstance(format_imports([]), list)
        input_param = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT

        self.assertEqual(format_imports(input_param), output)


class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__B815EEFBE4(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)

    def test__get_imports_from_docstring__5A0D9E6BC7(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        empty_example_passage = ''
        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])


class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__047B97CCC8(self):
        empty_example_passage = ''
        self.assertEqual(get_variables_from_docstring(empty_example_passage), '')

    def test__get_variables_from_docstring__34138EF052(self):
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)


class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__2BFFE43AC4(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(''), [])

    def test__stack_examples__2CDFB7C509(self):
        self.assertIsInstance(stack_examples([]), list)
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])

    def test__stack_examples__1957DF3889(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(['1) func_do_work()']), [])


class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__1DD2A843F8(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        self.assertEqual(get_params_from_docstring(''), [])

    def test__get_params_from_docstring__EB16B9484B(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)


class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__94E0B4C626(self):
        self.assertEqual(get_return_from_docstring(''), None)

    def test__get_return_from_docstring__AC31949F08(self):
        statements = TestBodies.RETURN_TYPE_TEST
        self.assertEqual(get_return_from_docstring(statements), 'int')


class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__FE5AB1B2BD(self):
        self.assertIsInstance(get_test_case_examples(''), list)
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)


class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__32197FA47F(self):
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)

    def test__get_test_from_example_passage__B15FF9130E(self):
        self.assertEqual(get_test_from_example_passage(None), None)

    def test__get_test_from_example_passage__CB43622455(self):
        self.assertEqual(get_test_from_example_passage('lorem ipsum'), None)
