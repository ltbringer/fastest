from fastest.constants import TestBodies
from fastest.test_compiler.compile_tests import add_imports_for_test_case
from fastest.test_compiler.compile_tests import create_test_class
import unittest

class TestCompileTestsAddImportsForTestCase(unittest.TestCase):
    def test__add_imports_for_test_case__F0955CF53A(self):        
        empty_test = { 'imports': None }
        test = { 'imports': ['from datetime import datetime'] }
        imports = {'import numpy as np'}
        updated_imports = {'import numpy as np', 'from datetime import datetime'}
        

        self.assertEqual(add_imports_for_test_case(empty_test, imports), imports)
    def test__add_imports_for_test_case__2DBB5AB4A8(self):        
        empty_test = { 'imports': None }
        test = { 'imports': ['from datetime import datetime'] }
        imports = {'import numpy as np'}
        updated_imports = {'import numpy as np', 'from datetime import datetime'}
        

        self.assertEqual(add_imports_for_test_case(test, imports), updated_imports)

class TestCompileTestsCreateTestClass(unittest.TestCase):
    def test__create_test_class__E0716D7375(self):        
        imports = {'import random'}
        contents = ['']
        deps_import = 'fastest/__main__'
        function_object = TestBodies.MOCK_FUNCTION_OBJECT
        root_module_name = 'fastest'
        

        self.assertEqual(create_test_class(imports, contents, deps_import, function_object, root_module_name), TestBodies.CREATE_TEST_CLASS_RESULT)
