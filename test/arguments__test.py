import unittest

from fastest.code_assets.arguments import get_args


class Test_arguments_get_args(unittest.TestCase):
    def test__get_args__06E910A255(self):
        self.assertEqual(get_args(' (arg1, arg2) '), ['arg1', 'arg2'])
    
    def test__get_args__961764A808(self):
        self.assertEqual(get_args('(arg1, arg2)'), ['arg1', 'arg2'])
