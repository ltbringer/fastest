from fastest.code_assets.function import get_functions
import unittest

class Testfunctionget_functions(unittest.TestCase):
    def test__get_functions__EC05C50716(self):        
        page = 'def f(): return 1'
        

        self.assertEqual(get_functions(page), [{'name': 'f', 'tests': None}])

