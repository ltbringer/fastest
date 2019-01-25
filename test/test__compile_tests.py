from fastest.constants import TestBodies
from fastest.test_compiler.compile_tests import add_imports_for_test_case
from fastest.test_compiler.compile_tests import create_test_class
import unittest


class TestCompileTestsAddImportsForTestCase(unittest.TestCase):
    def test__add_imports_for_test_case__7EB7EA29E6(self):
        empty_test = {'imports': None}
        imports = {'import numpy as np'}

        self.assertEqual(add_imports_for_test_case(empty_test, imports), imports)

    def test__add_imports_for_test_case__108109FB19(self):
        test = {'imports': ['from datetime import datetime']}
        imports = {'import numpy as np'}
        updated_imports = {'import numpy as np', 'from datetime import datetime'}

        self.assertEqual(add_imports_for_test_case(test, imports), updated_imports)


class TestCompileTestsCreateTestClass(unittest.TestCase):
    def test__create_test_class__476570EE77(self):
        imports = {'import random'}
        contents = ['']
        deps_import = 'fastest/__main__'
        function_object = TestBodies.MOCK_FUNCTION_OBJECT
        root_module_name = 'fastest'

        self.assertEqual(create_test_class(imports, contents, deps_import, function_object, root_module_name),
                         TestBodies.CREATE_TEST_CLASS_RESULT)
