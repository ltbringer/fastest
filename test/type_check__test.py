import unittest

from fastest.case_labyrinth.type_check_detect.type_check import detect_type_check


class Test_type_check_detect_type_check(unittest.TestCase):
           
                
    def test__detect_type_check__1E0EFEED0E(self):
        self.assertEqual(detect_type_check(["if type(var) is str"], "var"), True)

    
    def test__detect_type_check__399810E535(self):
        self.assertEqual(detect_type_check(["if True"], "var"), False)

    