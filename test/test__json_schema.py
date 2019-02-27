from fuzzer.rest_fuzzer.json_schema import get_schema_for
from fuzzer.rest_fuzzer.json_schema import get_schema_for_dict
from fuzzer.rest_fuzzer.json_schema import get_schema_for_list
from fuzzer.rest_fuzzer.json_schema import get_schema_for_primitive
from fuzzer.rest_fuzzer.json_schema import make_schema_object
from fuzzer.rest_fuzzer.json_schema import schema_fn
from fuzzer.rest_fuzzer.json_schema import type_name
import unittest


class TestJsonSchemaTypeName(unittest.TestCase):
    def test__type_name__321A000F63(self):
        self.assertEqual(type_name('apple'), 'str')


class TestJsonSchemaSchemaFn(unittest.TestCase):
    def test__schema_fn__76ED5A360F(self):
        self.assertEqual(schema_fn("str"), get_schema_for_primitive)


class TestJsonSchemaGetSchemaForPrimitive(unittest.TestCase):
    def test__get_schema_for_primitive__A070E8DF88(self):
        self.assertEqual(get_schema_for_primitive('', ''), [])


class TestJsonSchemaGetSchemaForList(unittest.TestCase):
    def test__get_schema_for_list__76EB9EE50E(self):
        schema_object = {
            'inner': [{
                'inner': [],
                'name': 'key',
                'type': 'int'
            }],
            'name': '__auto__',
            'type': 'dict'
        }

        self.assertEqual(get_schema_for_list([{"key": 1}], "list"), schema_object)


class TestJsonSchemaGetSchemaForDict(unittest.TestCase):
    def test__get_schema_for_dict__7F4D19694B(self):
        self.assertEqual(get_schema_for_dict({'key': 1}, 'dict'), [{'type': 'int', 'inner': [], 'name': 'key'}])


class TestJsonSchemaGetSchemaFor(unittest.TestCase):
    def test__get_schema_for__E131A99969(self):
        self.assertEqual(get_schema_for({"key": 1}, 'dict'), [{'type': 'int', 'inner': [], 'name': 'key'}])


class TestJsonSchemaMakeSchemaObject(unittest.TestCase):
    def test__make_schema_object__C0A5822480(self):
        schema_object = {
            'inner': [{'inner': [], 'name': 'key', 'type': 'int'}],
            'name': '__root__',
            'type': 'dict'
        }

        self.assertEqual(make_schema_object({"key": 1}), schema_object)
