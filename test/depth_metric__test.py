import unittest

from fastest.code_style.depth_metric import is_function_too_long


class Test_depth_metric_is_function_too_long(unittest.TestCase):
           
                
    def test__is_function_too_long__D127952C1B(self):
        
        self.assertEqual(is_function_too_long("\n\n\n\n\n"), (False, 6))
        

    
    def test__is_function_too_long__D687449B35(self):
        
        self.assertEqual(is_function_too_long("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"), (True, 31))
        

    