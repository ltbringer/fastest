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
    def test__format_imports__3EAC419E70(self):
        self.assertIsInstance(format_imports([]), list)
        input_imports = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT
        self.assertEqual(format_imports(input_imports), output)


class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__3F42634A28(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)

    def test__get_imports_from_docstring__5BBF6F1A0B(self):
        self.assertIsInstance(get_imports_from_docstring(''), list)
        empty_example_passage = ''

        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])


class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__1D4A7198C0(self):
        self.assertIsInstance(get_variables_from_docstring(''), list)
        empty_example_passage = ''
        self.assertEqual(get_variables_from_docstring(empty_example_passage), [])

    def test__get_variables_from_docstring__8E7DC1ED19(self):
        self.assertIsInstance(get_variables_from_docstring(''), list)
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)


class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__0EFA46A2DD(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(''), [])

    def test__stack_examples__67BEEC26D3(self):
        self.assertIsInstance(stack_examples([]), list)
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])

    def test__stack_examples__AD9B9CE694(self):
        self.assertIsInstance(stack_examples([]), list)
        self.assertEqual(stack_examples(['1) func_do_work()']), [])


class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__BC9B4A672A(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        self.assertEqual(get_params_from_docstring(''), [])

    def test__get_params_from_docstring__BC9E12F843(self):
        self.assertIsInstance(get_params_from_docstring(''), list)
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)


class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__D6EAB82C9F(self):
        self.assertIsInstance(get_return_from_docstring(''), str)
        self.assertEqual(get_return_from_docstring(''), '')

    def test__get_return_from_docstring__A64BF5C1E6(self):
        self.assertIsInstance(get_return_from_docstring(''), str)
        statements = TestBodies.RETURN_TYPE_TEST
        self.assertEqual(get_return_from_docstring(statements), 'int')


class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__D3C433C79E(self):
        self.assertIsInstance(get_test_case_examples(''), list)
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)


class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__A2D8B556B1(self):
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)

    def test__get_test_from_example_passage__5EDE736509(self):
        self.assertEqual(get_test_from_example_passage(None), {})

    def test__get_test_from_example_passage__620AE1F8F0(self):
        self.assertEqual(get_test_from_example_passage('lorem ipsum'), {})
