import os
from fastest.bodies import f
from fastest.constants import CONTENT, KEYS, SYS




def add_imports_for_test_case(test, imports):
    if test[KEYS.IMPORTS] is None:
        return imports
    for import_statement in test[KEYS.IMPORTS]:
        imports.add(import_statement)
    return imports

def create_test_class(imports, contents, deps_import, function_object, root_module_name):
    if len(function_object[KEYS.TESTS]) == 0:
        return None

    imports.add(CONTENT.IMPORT_UNITTEST)
    imports.add(CONTENT.DEPS_IMPORT_TEMPLATE.format(deps_import, function_object[KEYS.NAME]))
    contents.append(CONTENT.CLASS_CREATE_TEMPLATE.format(root_module_name, function_object[KEYS.NAME]))
    return imports, contents


def create_test_case_content(function_object, imports, contents):
    for example in function_object[KEYS.TESTS][KEYS.EXAMPLES]:
        contents.append(f.create_naive_test_case(function_object, example))
    imports = add_imports_for_test_case(function_object[KEYS.TESTS], imports)
    return imports, contents


def create_test_case(function_objects, deps_import, root_module_name):
    imports = set()
    contents = []

    for function_object in function_objects:
        if function_object is None:
            continue

        if function_object[KEYS.TESTS] is None:
            continue

        imports, contents = create_test_class(imports, contents, deps_import, function_object, root_module_name)
        imports, contents = create_test_case_content(function_object, imports, contents)
    return imports, contents


def write_tests_to_file(fp, imports, contents):
    return fp.write(''.join(sorted(list(imports)) + contents))


def build(function_objects, src_file_path, base_path):
    last_file = -1
    test_file_name = src_file_path.split(SYS.SLASH)[last_file].replace('.py', SYS.TEST_FILE_ENDING)
    deps_import = src_file_path.replace(base_path + SYS.SLASH, '').replace(SYS.SLASH, '.').replace('.py', '')
    root_module_name = deps_import.split('.')[-1]
    test_file_path = os.path.join(base_path, KEYS.TEST, test_file_name)


    with open(test_file_path, 'w+') as fp:
        imports, contents = create_test_case(function_objects, deps_import, root_module_name)
        write_tests_to_file(fp, imports, contents)
