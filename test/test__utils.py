from fastest.utils import count_truthy
from fastest.utils import to_camel_case
import unittest


class TestUtilsCountTruthy(unittest.TestCase):
    def test__count_truthy__956FC1B716(self):
        self.assertIsInstance(count_truthy([]), int)
        self.assertEqual(count_truthy([1, 2, None, 'a']), 3)

    def test__count_truthy__0F68040A54(self):
        self.assertIsInstance(count_truthy([]), int)
        self.assertEqual(count_truthy([1, 2, 0, 'a']), 4)


class TestUtilsToCamelCase(unittest.TestCase):
    def test__to_camel_case__2ABC8D7B37(self):
        self.assertIsInstance(to_camel_case(''), str)
        self.assertEqual(to_camel_case('snake_cased_string'), 'SnakeCasedString')
