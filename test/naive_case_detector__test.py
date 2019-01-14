import unittest

from fastest.code_assets.naive_case_detector import get_naive_case


class Test_naive_case_detector_get_naive_case(unittest.TestCase):
           
                
    def test__get_naive_case__B57CDDF269(self):
        self.assertEqual(get_naive_case("example: fn_do_work() -> 8 #"),  [{
        "from": "fn_do_work()",
        "expect": '8'
    }])
        
    

    