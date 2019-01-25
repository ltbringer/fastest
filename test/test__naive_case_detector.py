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
    def test__format_imports__9EE38D0EC1(self):
        input_imports = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT

        self.assertEqual(format_imports(input_imports), output)


class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__0A97C6C157(self):
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION

        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)

    def test__get_imports_from_docstring__6714B5906D(self):
        empty_example_passage = ''

        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])


class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__AEB1E37830(self):
        empty_example_passage = ''

        self.assertEqual(get_variables_from_docstring(empty_example_passage), '')

    def test__get_variables_from_docstring__B3CB6ACE59(self):
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT

        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)


class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__E99E139CF4(self):
        self.assertEqual(stack_examples(''), [])

    def test__stack_examples__77FB0AEFA4(self):
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])


class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__75FCBBAE6C(self):
        self.assertEqual(get_params_from_docstring(''), [])

    def test__get_params_from_docstring__D01A5D4D7A(self):
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST

        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)


class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__C55EDAEA80(self):
        self.assertEqual(get_return_from_docstring(''), None)

    def test__get_return_from_docstring__3AFD7DDF98(self):
        statements = TestBodies.RETURN_TYPE_TEST

        self.assertEqual(get_return_from_docstring(statements), 'int')


class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__B12AC7941B(self):
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE

        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)


class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__786D0BA0F1(self):
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT

        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)

    def test__get_test_from_example_passage__D2A0AD99BE(self):

        self.assertEqual(get_test_from_example_passage(None), None)

    def test__get_test_from_example_passage__4A60B432CB(self):

        self.assertEqual(get_test_from_example_passage('lorem ipsum'), None)
