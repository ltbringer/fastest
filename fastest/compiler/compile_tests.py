import os
from fastest.bodies import f


def build(function_objects, src_file_path, base_path):
    test_file_name = src_file_path.split('/')[-1].replace('.py', '__test.py')
    deps_import = src_file_path.replace(base_path + '/', '').replace('/', '.').replace('.py', '')
    root_module_name = deps_import.split('.')[-1]
    test_file_path = os.path.join(base_path, 'test', test_file_name)

    with open(test_file_path, 'w+') as fp:
        fp.write('import unittest\n\n')
        for function_object in function_objects:
            fp.write('from {} import {}\n'.format(deps_import, function_object['name']))

        for function_object in function_objects:
            fp.write("""\n
class Test_{}_{}(unittest.TestCase):""".format(root_module_name, function_object['name']))
            for test in function_object['tests']:
                fp.write(f.create_naive_test_case(function_object, test))
