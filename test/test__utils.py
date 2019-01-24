from fastest.utils import count_truthy
from fastest.utils import to_camel_case
import unittest


class TestUtilsCountTruthy(unittest.TestCase):
    def test__count_truthy__DB40D6FA9F(self):
        self.assertIsInstance(count_truthy([]), int)
        self.assertEqual(count_truthy([1, 2, None, 'a']), 3)

    def test__count_truthy__73AFF983FB(self):
        self.assertIsInstance(count_truthy([]), int)
        self.assertEqual(count_truthy([1, 2, 0, 'a']), 4)


class TestUtilsToCamelCase(unittest.TestCase):
    def test__to_camel_case__980D6D2AC9(self):
        self.assertIsInstance(to_camel_case(''), str)
        self.assertEqual(to_camel_case('snake_cased_string'), 'SnakeCasedString')
