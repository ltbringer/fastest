from fastest.utils import count_truthy
from fastest.utils import to_camel_case
import unittest

class TestUtilsCountTruthy(unittest.TestCase):
    def test__count_truthy__69C9161EC6(self):
        self.assertEqual(count_truthy([1, 2, None, 'a']), 3)
    def test__count_truthy__6F3F26F9F1(self):
        self.assertEqual(count_truthy([1, 2, 0, 'a']), 4)

class TestUtilsToCamelCase(unittest.TestCase):
    def test__to_camel_case__EB404A115B(self):
        self.assertEqual(to_camel_case('snake_cased_string'), 'SnakeCasedString')
