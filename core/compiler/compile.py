import os
from core.bodies import f


def build(function_objects, src_file_path, base_path):
    test_file_path = src_file_path.replace('.py', '__test.py')
    deps_import = src_file_path.replace(base_path + '/', '').replace('/', '.').replace('.py', '')

    with open(test_file_path, 'w+') as fp:
        fp.write('import unittest\n\n')
        for function_object in function_objects:
            fp.write('from {} import {}\n'.format(deps_import, function_object['name']))

        for function_object in function_objects:
            fp.write(
                """\n
class Test_{}(unittest.TestCase):
           
                """.format(function_object['name'])
            )
            for arg in function_object['args']:
                fp.write(
                    f.create_var_type_test_case(
                        function_object, arg, function_object['str']
                    ))
            fp.write(
                f.create_return_type_test_case(
                    function_object,
                    function_object['returns'],
                    function_object['str']
                ))

