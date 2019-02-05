from fastest.code_assets.naive_case_detector import format_imports
from fastest.code_assets.naive_case_detector import get_exception_case_from_examples
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
    def test__format_imports__4E4528970A(self):
        import_input = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT

        self.assertEqual(format_imports(import_input), output)


class TestNaiveCaseDetectorGetExceptionCaseFromExamples(unittest.TestCase):
    def test__get_exception_case_from_examples__FBE435B301(self):
        exception_example_happy_case = TestBodies.EXCEPTION_EXAMPLE_HAPPY_CASE
        happy_case_output = TestBodies.EXCEPTION_HAPPY_CASE_OUTPUT

        self.assertEqual(get_exception_case_from_examples(exception_example_happy_case), happy_case_output)

    def test__get_exception_case_from_examples__C57578CEB4(self):
        exception_example_sep_missing = TestBodies.EXCEPTION_EXAMPLE_SEP_MISSING
        self.assertEqual(get_exception_case_from_examples(exception_example_sep_missing), [])

    def test__get_exception_case_from_examples__B08C87B424(self):
        self.assertRaises(Exception, get_exception_case_from_examples, None)


class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__DCDFC0CDF9(self):
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)

    def test__get_imports_from_docstring__96DC60F806(self):
        empty_example_passage = ''
        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])


class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__DBE5A26310(self):
        empty_example_passage = ''
        self.assertEqual(get_variables_from_docstring(empty_example_passage), [])

    def test__get_variables_from_docstring__14EC57141E(self):
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)


class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__A63E1E9CC4(self):
        self.assertEqual(stack_examples(''), [])

    def test__stack_examples__7032208007(self):
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])

    def test__stack_examples__4B50A00EED(self):
        self.assertEqual(stack_examples(['1) func_do_work()']), [])


class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__1AF44836EB(self):
        self.assertEqual(get_params_from_docstring(''), [])

    def test__get_params_from_docstring__54FD208434(self):
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)


class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__91261F2FD0(self):
        self.assertEqual(get_return_from_docstring(''), '')

    def test__get_return_from_docstring__8E61F6F8CC(self):
        statements = TestBodies.RETURN_TYPE_TEST
        self.assertEqual(get_return_from_docstring(statements), 'int')


class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__F24FA72236(self):
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)


class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__88E30AA8BD(self):
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)

    def test__get_test_from_example_passage__4CA339D67D(self):
        self.assertEqual(get_test_from_example_passage(None), {})

    def test__get_test_from_example_passage__C2A0A385B6(self):
        self.assertEqual(get_test_from_example_passage('lorem ipsum'), {})
