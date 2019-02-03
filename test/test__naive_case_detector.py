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
    def test__format_imports__F35E73FA38(self):
        self.assertIsInstance(format_imports([]), list)
        import_input = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT

        self.assertEqual(format_imports(import_input), output)


class TestNaiveCaseDetectorGetExceptionCaseFromExamples(unittest.TestCase):
    def test__get_exception_case_from_examples__1C4CDE4697(self):
        self.assertIsInstance(get_exception_case_from_examples(''), list)
        exception_example_happy_case = TestBodies.EXCEPTION_EXAMPLE_HAPPY_CASE
        happy_case_output = TestBodies.EXCEPTION_HAPPY_CASE_OUTPUT

        self.assertEqual(get_exception_case_from_examples(exception_example_happy_case), happy_case_output)

    def test__get_exception_case_from_examples__06F8A62212(self):
        self.assertIsInstance(get_exception_case_from_examples(''), list)
        exception_example_sep_missing = TestBodies.EXCEPTION_EXAMPLE_SEP_MISSING
        self.assertEqual(get_exception_case_from_examples(exception_example_sep_missing), [])

    def test__get_exception_case_from_examples__C6D6C4611C(self):
        self.assertIsInstance(get_exception_case_from_examples(''), list)
        self.assertRaises(TypeError, get_exception_case_from_examples, *[None])


class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__3FC97483F1(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)

    def test__get_imports_from_docstring__4B01345AB8(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        empty_example_passage = ''

        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])


class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__CE044B4DD9(self):
        self.assertIsInstance(get_variables_from_docstring(''), list)
        empty_example_passage = ''

        self.assertEqual(get_variables_from_docstring(empty_example_passage), [])

    def test__get_variables_from_docstring__035ECC717E(self):
        self.assertIsInstance(get_variables_from_docstring(''), list)
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT

        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)


class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__FB24DF16EB(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(''), [])

    def test__stack_examples__7C6CAD261B(self):
        self.assertIsInstance(stack_examples([]), list)
        example_strings = TestBodies.STACK_EXAMPLES_TEST

        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])

    def test__stack_examples__04F976F902(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(['1) func_do_work()']), [])


class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__4F5FAAB92D(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        self.assertEqual(get_params_from_docstring(''), [])

    def test__get_params_from_docstring__3C0D0B8AE3(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)


class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__47901F62D9(self):
        self.assertIsInstance(get_return_from_docstring(''), str)
        self.assertEqual(get_return_from_docstring(''), '')

    def test__get_return_from_docstring__2A01DA18F3(self):
        self.assertIsInstance(get_return_from_docstring(''), str)
        statements = TestBodies.RETURN_TYPE_TEST
        self.assertEqual(get_return_from_docstring(statements), 'int')


class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__4100F9189F(self):
        self.assertIsInstance(get_test_case_examples(''), list)
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)


class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__10444B1A46(self):
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)

    def test__get_test_from_example_passage__0234026012(self):
        self.assertEqual(get_test_from_example_passage(None), {})

    def test__get_test_from_example_passage__F07AE3937C(self):
        self.assertEqual(get_test_from_example_passage('lorem ipsum'), {})
