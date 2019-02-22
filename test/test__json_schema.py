from fastest.rest_fuzzer.json_schema import get_schema_for
from fastest.rest_fuzzer.json_schema import get_schema_for_dict
from fastest.rest_fuzzer.json_schema import get_schema_for_list
from fastest.rest_fuzzer.json_schema import get_schema_for_primitive
from fastest.rest_fuzzer.json_schema import make_schema_object
from fastest.rest_fuzzer.json_schema import schema_fn
from fastest.rest_fuzzer.json_schema import type_name
import unittest

class TestJsonSchemaTypeName(unittest.TestCase):
    def test__type_name__5313FC4E00(self):
        self.assertEqual(type_name('apple'), 'str')

class TestJsonSchemaSchemaFn(unittest.TestCase):
    def test__schema_fn__77FB22598D(self):
        self.assertEqual(schema_fn("str"), get_schema_for_primitive)

class TestJsonSchemaGetSchemaForPrimitive(unittest.TestCase):
    def test__get_schema_for_primitive__6A3023DB00(self):
        self.assertEqual(get_schema_for_primitive('', ''), None)

class TestJsonSchemaGetSchemaForList(unittest.TestCase):
    def test__get_schema_for_list__B0C646A2CF(self):        
        schema_object = {
            'inner': [{
                'inner': None,
                'name': 'key',
                'type': 'int'
            }],
            'name': '__auto__',
            'type': 'dict'
        }
        

        self.assertEqual(get_schema_for_list([{"key": 1}], "list"), schema_object)

class TestJsonSchemaGetSchemaForDict(unittest.TestCase):
    def test__get_schema_for_dict__5F2E8720CA(self):
        self.assertEqual(get_schema_for_dict({'key': 1}, 'dict'), [{'type': 'int', 'inner': None, 'name': 'key'}])

class TestJsonSchemaGetSchemaFor(unittest.TestCase):
    def test__get_schema_for__B2B60F58A8(self):
        self.assertEqual(get_schema_for({"key": 1}, 'dict'), [{'type': 'int', 'inner': None, 'name': 'key'}])

class TestJsonSchemaMakeSchemaObject(unittest.TestCase):
    def test__make_schema_object__0F14007CF7(self):        
        schema_object = {
            'inner': [{'inner': None, 'name': 'key', 'type': 'int'}],
            'name': '__root__',
            'type': 'dict'
        }
        

        self.assertEqual(make_schema_object({"key": 1}), schema_object)
