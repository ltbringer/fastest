import unittest

from fastest.code_assets.function import get_functions


class Test_function_get_functions(unittest.TestCase):
           
                
    def test__get_functions__DD5E6A1F94(self):
        
    # testers notes:
    # --------------
    # Your function has 23 lines of code, it is strongly advised to break them
    # when they are doing too many operations.
    


        self.assertEqual(get_functions("def fn(arg1, arg2):\narg1 += 1\n\treturn arg1 + arg2"), [{
        'name': 'fn',
        'args': ['arg1', 'arg2'],
        'str': 'def fn(arg1, arg2):\n\treturn arg1 + arg2',
        'vars': [],
        'tests': []
    }])
        

    