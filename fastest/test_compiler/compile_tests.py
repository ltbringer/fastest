from fastest.constants import Content, Keys
from fastest.utils import to_camel_case


def add_imports_for_test_case(test, imports):
    """
    ---
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    empty_test = { 'imports': None }
    test = { 'imports': ['from datetime import datetime'] }
    imports = {'import numpy as np'}
    updated_imports = {'import numpy as np', 'from datetime import datetime'}
    @end

    1) add_imports_for_test_case(empty_test, imports) -> imports
    2) add_imports_for_test_case(test, imports) -> updated_imports
    ---
    :param test: dict
    :param imports: set
    :return: set
    """
    if test.get(Keys.IMPORTS) is None:
        return imports
    for import_statement in test.get(Keys.IMPORTS):
        imports.add(import_statement)
    return imports


def create_test_class(imports, contents, deps_import, function_object, root_module_name):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    imports = {'import random'}
    contents = ['']
    deps_import = 'fastest/__main__'
    function_object = TestBodies.MOCK_FUNCTION_OBJECT
    root_module_name = 'fastest'
    @end

    1) create_test_class(imports, contents, deps_import, function_object, root_module_name) -> TestBodies.CREATE_TEST_CLASS_RESULT
    ----
    :param imports: set
    :param contents: list
    :param deps_import: str
    :param function_object: dict
    :param root_module_name: str
    :return: tuple
    """
    imports.add(Content.IMPORT_UNITTEST)
    imports.add(Content.DEPS_IMPORT_TEMPLATE.format(deps_import, function_object.get(Keys.NAME)))
    camel_cased_root_module_name = to_camel_case(root_module_name)
    camel_cased_function_name = to_camel_case(function_object.get(Keys.NAME, ''))
    contents.append(Content.CLASS_CREATE_TEMPLATE.format(
        camel_cased_root_module_name, camel_cased_function_name
    ))
    return imports, contents
