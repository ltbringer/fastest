import unittest

from fastest.code_assets.return_value import get_return_values


class Test_return_value_get_return_values(unittest.TestCase):
    def test__get_return_values__1C52293743(self):
        self.assertEqual(get_return_values('return 5'), ['5'])

    def test__get_return_values__3FF421998A(self):
        self.assertEqual(get_return_values(''), [None])
