import os
from fastest.bodies import test_case_template_builder
from fastest.constants import Content, Keys, Sys
from fastest.utils import to_camel_case


def add_imports_for_test_case(test, imports):
    if test[Keys.IMPORTS] is None:
        return imports
    for import_statement in test[Keys.IMPORTS]:
        imports.add(import_statement)
    return imports


def create_test_class(imports, contents, deps_import, function_object, root_module_name):
    imports.add(Content.IMPORT_UNITTEST)
    imports.add(Content.DEPS_IMPORT_TEMPLATE.format(deps_import, function_object[Keys.NAME]))
    camel_cased_root_module_name = to_camel_case(root_module_name)
    camel_cased_function_name = to_camel_case(function_object[Keys.NAME])
    contents.append(Content.CLASS_CREATE_TEMPLATE.format(
        camel_cased_root_module_name, camel_cased_function_name
    ))
    return imports, contents


def create_test_case_content(function_object, imports, contents):
    for example in function_object[Keys.TESTS][Keys.EXAMPLES]:
        contents.append(test_case_template_builder.create_naive_test_case(function_object, example))

    imports = add_imports_for_test_case(function_object[Keys.TESTS], imports)
    return imports, contents


def create_test_case(function_objects, deps_import, root_module_name):
    imports = set()
    contents = []

    for function_object in function_objects:
        if type(function_object) is not dict:
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
