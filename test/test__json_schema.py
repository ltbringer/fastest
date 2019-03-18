from fuzzer.rest_fuzzer.json_schema import get_schema_for
from fuzzer.rest_fuzzer.json_schema import get_schema_for_dict
from fuzzer.rest_fuzzer.json_schema import get_schema_for_list
from fuzzer.rest_fuzzer.json_schema import get_schema_for_primitive
from fuzzer.rest_fuzzer.json_schema import make_schema_object
from fuzzer.rest_fuzzer.json_schema import schema_fn
from fuzzer.rest_fuzzer.json_schema import type_name
import unittest

class TestJsonSchemaTypeName(unittest.TestCase):
    def test__type_name__24845E27E9(self):
        self.assertEqual(type_name('apple'), 'str')

class TestJsonSchemaSchemaFn(unittest.TestCase):
    def test__schema_fn__E1944D0564(self):
        self.assertEqual(schema_fn("str"), get_schema_for_primitive)

class TestJsonSchemaGetSchemaForPrimitive(unittest.TestCase):
    def test__get_schema_for_primitive__9CEA5E7C95(self):
        self.assertEqual(get_schema_for_primitive('', '', []), (0.1, []))

class TestJsonSchemaGetSchemaForList(unittest.TestCase):
    def test__get_schema_for_list__B9530483F7(self):        
        schema_object = (0.1, {
            'inner': (0.1, [{
                'inner':  (0.1, []),
                'name': 'key',
                'type': 'int'
            }]),
            'name': '__auto__',
            'type': 'dict'
        })
        

        self.assertEqual(get_schema_for_list([{"key": 1}], "list", []), schema_object)

class TestJsonSchemaGetSchemaForDict(unittest.TestCase):
    def test__get_schema_for_dict__BF69A076E4(self):        
        schema_obj = (0.1, [{
            'inner': (0.1, []),
            'type': 'int',
            'name': 'key'
        }])
        

        self.assertEqual(get_schema_for_dict({'key': 1}, 'dict', []), schema_obj)

class TestJsonSchemaGetSchemaFor(unittest.TestCase):
    def test__get_schema_for__71B0DC8675(self):        
        schema_obj = (0.1, [{
            'type': 'int',
            'inner': (0.1, []),
            'name': 'key'
        }])
        

        self.assertEqual(get_schema_for({"key": 1}, 'dict', []), schema_obj)

class TestJsonSchemaMakeSchemaObject(unittest.TestCase):
    def test__make_schema_object__8F980E2E86(self):        
        schema_object = (
            [0.1, 0.1, 0.1],
            {
                'inner': (0.1, [{
                    'inner': (0.1, []),
                    'name': 'key',
                    'type': 'int'
                }]),
                'name': '__root__',
                'type': 'dict'
            }
        )
        
        

        self.assertEqual(make_schema_object({"key": 1}), schema_object)
