import unittest

from fastest.type.type_inference import infer


class Test_type_inference_infer(unittest.TestCase):
    def test__infer__D9646751F7(self):
        self.assertEqual(infer("list_var", "def fn():\n\tlist_var = [1]"), ['list'])

    def test__infer__C3C15E03D4(self):
        self.assertEqual(infer("some_var", "def fn():\n\tsome_var + some_other"), ['int', 'str'])
