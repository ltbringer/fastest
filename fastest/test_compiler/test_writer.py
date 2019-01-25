import os
from fastest.constants import Keys, Sys
from fastest.test_compiler.compile_tests import add_imports_for_test_case, create_test_class
from fastest.bodies.test_case_template_builder import create_naive_test_case


def create_test_case_content(function_object, imports, contents):
    """
    :param function_object: dict
    :param imports: set
    :param contents: list
    :return: tuple
    """
    for example in function_object[Keys.TESTS][Keys.EXAMPLES]:
        contents.append(create_naive_test_case(function_object, example))

    imports = add_imports_for_test_case(function_object[Keys.TESTS], imports)
    return imports, contents


def create_test_case(function_objects, deps_import, root_module_name):
    imports = set()
    contents = []

    for function_object in function_objects:
        if not isinstance(function_object, dict):
            continue
        if function_object[Keys.TESTS] is None:
            continue
        imports, contents = create_test_class(imports, contents, deps_import, function_object, root_module_name)
        imports, contents = create_test_case_content(function_object, imports, contents)
    return imports, contents


def write_tests_to_file(fp, imports, contents):
    return fp.write(''.join(sorted(list(imports)) + contents))


def build(function_objects, src_file_path, base_path):
    last_file = -1
    test_file_name = 'test__' + src_file_path.split(Sys.SLASH)[last_file]
    deps_import = src_file_path.replace(base_path + Sys.SLASH, '').replace(Sys.SLASH, '.').replace('.py', '')
    root_module_name = deps_import.split('.')[-1]
    test_file_path = os.path.join(base_path, Keys.TEST, test_file_name)

    with open(test_file_path, 'w+') as fp:
        imports, contents = create_test_case(function_objects, deps_import, root_module_name)
        write_tests_to_file(fp, imports, contents)
