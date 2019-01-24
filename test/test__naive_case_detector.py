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
    def test__format_imports__69A933D7CC(self):        
        input = TestBodies.TEST_STACK_IMPORTS_INPUT
        output = TestBodies.TEST_STACK_IMPORTS_OUTPUT
        

        self.assertEqual(format_imports(input), output)

class TestNaiveCaseDetectorGetImportsFromDocstring(unittest.TestCase):
    def test__get_imports_from_docstring__A42D97486E(self):        
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        empty_example_passage = ''
        

        self.assertEqual(get_imports_from_docstring(example_passage), import_statements)
    def test__get_imports_from_docstring__195D71945A(self):        
        example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
        import_statements = TestBodies.TEST_IMPORT_EXTRACTION
        empty_example_passage = ''
        

        self.assertEqual(get_imports_from_docstring(empty_example_passage), [])

class TestNaiveCaseDetectorGetVariablesFromDocstring(unittest.TestCase):
    def test__get_variables_from_docstring__B50FFF3432(self):        
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        empty_example_passage = ''
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
        

        self.assertEqual(get_variables_from_docstring(empty_example_passage), '')
    def test__get_variables_from_docstring__F8470C1CF0(self):        
        example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
        empty_example_passage = ''
        expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
        

        self.assertEqual(get_variables_from_docstring(example_passage), expected_output)

class TestNaiveCaseDetectorStackExamples(unittest.TestCase):
    def test__stack_examples__49154AE36B(self):        
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        

        self.assertEqual(stack_examples(''), [])
    def test__stack_examples__410CF9BB5B(self):        
        example_strings = TestBodies.STACK_EXAMPLES_TEST
        

        self.assertEqual(stack_examples(example_strings), [{'expect': '25', 'from': 'square(5)'}])

class TestNaiveCaseDetectorGetParamsFromDocstring(unittest.TestCase):
    def test__get_params_from_docstring__5A150C24B6(self):        
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        

        self.assertEqual(get_params_from_docstring(''), [])
    def test__get_params_from_docstring__9D7E8E645D(self):        
        statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
        

        self.assertEqual(get_params_from_docstring(statements), TestBodies.EXPECT_PARAMS)

class TestNaiveCaseDetectorGetReturnFromDocstring(unittest.TestCase):
    def test__get_return_from_docstring__BA86CDDC64(self):        
        statements = TestBodies.RETURN_TYPE_TEST
        

        self.assertEqual(get_return_from_docstring(''), None)
    def test__get_return_from_docstring__4F3FC6AE04(self):        
        statements = TestBodies.RETURN_TYPE_TEST
        

        self.assertEqual(get_return_from_docstring(statements), 'int')

class TestNaiveCaseDetectorGetTestCaseExamples(unittest.TestCase):
    def test__get_test_case_examples__DBCDB01A79(self):        
        example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
        

        self.assertEqual(get_test_case_examples(example_passage), TestBodies.TEST_EXAMPLE_PASSAGE_RESULT)

class TestNaiveCaseDetectorGetTestFromExamplePassage(unittest.TestCase):
    def test__get_test_from_example_passage__7427939E7E(self):        
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        

        self.assertEqual(get_test_from_example_passage(statements), TestBodies.NAIVE_CASE_TEST_RESULT)
    def test__get_test_from_example_passage__3E8BC2BB19(self):        
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        

        self.assertEqual(get_test_from_example_passage(None), None)
    def test__get_test_from_example_passage__8F42AC2F6D(self):        
        statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
        

        self.assertEqual(get_test_from_example_passage('lorem ipsum'), None)
