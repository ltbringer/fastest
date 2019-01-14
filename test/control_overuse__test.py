import unittest

from fastest.code_style.control_overuse import has_too_many_if_statements
from fastest.code_style.control_overuse import get_indent_of_loop
from fastest.code_style.control_overuse import get_statements_from_function_body
from fastest.code_style.control_overuse import count_loop_indents
from fastest.code_style.control_overuse import get_loop_complexity


class Test_control_overuse_has_too_many_if_statements(unittest.TestCase):
           
                
    def test__has_too_many_if_statements__5A97584B89(self):
        
    # testers notes:
    # --------------
    # Your function has 16 conditions, it is strongly advised to convert them
    # to individual functions. It is likely that they are doing different tasks.
    


        self.assertEqual(has_too_many_if_statements("if \nif \nif \nif \nif \nif \nif "), (True, 7))
        

    
    def test__has_too_many_if_statements__6CD18D0270(self):
        
    # testers notes:
    # --------------
    # Your function has 16 conditions, it is strongly advised to convert them
    # to individual functions. It is likely that they are doing different tasks.
    


        self.assertEqual(has_too_many_if_statements("if if if"), (False, 3))
        

    

class Test_control_overuse_get_indent_of_loop(unittest.TestCase):
           
                
    def test__get_indent_of_loop__A08A2D9E2F(self):
        
        self.assertEqual(get_indent_of_loop("   for i in range(10):"), 3)
        

    

class Test_control_overuse_get_statements_from_function_body(unittest.TestCase):
           
                
    def test__get_statements_from_function_body__0520D46989(self):
        
        self.assertEqual(get_statements_from_function_body("a\n b"), ['a', ' b'])
        

    

class Test_control_overuse_count_loop_indents(unittest.TestCase):
           
                
    def test__count_loop_indents__F6614EBB22(self):
        
        self.assertEqual(count_loop_indents("   for i in range(1):"), [3])
        

    

class Test_control_overuse_get_loop_complexity(unittest.TestCase):
           
                
    def test__get_loop_complexity__0A881061A5(self):
        
        self.assertEqual(get_loop_complexity("   for i in range(1):\n       for i in range(1):"), (False, 1))
        

    