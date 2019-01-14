import unittest

from fastest.type.type_usage_patterns import used_as_int
from fastest.type.type_usage_patterns import used_as_str
from fastest.type.type_usage_patterns import used_as_iterable
from fastest.type.type_usage_patterns import used_as_list
from fastest.type.type_usage_patterns import used_as_tuple
from fastest.type.type_usage_patterns import used_as_dict


class Test_type_usage_patterns_used_as_int(unittest.TestCase):
    def test__used_as_int__111EE739FF(self):
        self.assertEqual(used_as_int("a = 4", "a"), 1)

    def test__used_as_int__E0437A01FB(self):
        self.assertEqual(used_as_int("a + 4", "a"), 1)

    def test__used_as_int__E27DB6D8FE(self):
        self.assertEqual(used_as_int("a * 4", "a"), 1)

    def test__used_as_int__D40B555144(self):
        self.assertEqual(used_as_int("a - 4", "a"), 1)


class Test_type_usage_patterns_used_as_str(unittest.TestCase):
    def test__used_as_str__014F1AB308(self):
        self.assertEqual(used_as_str("string_var + 'something'", "string_var"), 1)

    def test__used_as_str__930DB851F7(self):
        self.assertEqual(used_as_str("string_var * 5", "string_var"), 1)


class Test_type_usage_patterns_used_as_iterable(unittest.TestCase):
    def test__used_as_iterable__55E3D3C962(self):
        self.assertEqual(used_as_iterable("for word in words", "words"), 1)


class Test_type_usage_patterns_used_as_list(unittest.TestCase):
    def test__used_as_list__38977D6942(self):
        self.assertEqual(used_as_list("apples.append(10)", "apples"), 1)

    def test__used_as_list__F338574B6A(self):
        self.assertEqual(used_as_list("apples = [11, 12]", "apples"), 1)


class Test_type_usage_patterns_used_as_tuple(unittest.TestCase):
    def test__used_as_tuple__DA01BD0FF3(self):
        self.assertEqual(used_as_tuple("words = (11, 2)", "words"), 1)


class Test_type_usage_patterns_used_as_dict(unittest.TestCase):
    def test__used_as_dict__5A65855176(self):
        self.assertEqual(used_as_dict("dict_input['val']", "dict_input"), 1)
