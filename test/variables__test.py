import unittest

from fastest.code_assets.variables import get_variables


class Test_variables_get_variables(unittest.TestCase):
    def test__get_variables__B87760F28E(self):
        self.assertEqual(get_variables("def fn(arg1, arg2):\n\tc = 4\n\treturn arg1 + arg2", ["arg1", "arg2"]), ["c"])
