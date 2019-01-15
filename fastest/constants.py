import platform


class SYS:
    __UNIX_SLASH = '/'
    __WINDOWS_SLASH = '\\'
    PY = '.py'
    SLASH = __WINDOWS_SLASH if platform.system == 'Windows' else __UNIX_SLASH
    TEST_FILE_ENDING = '__test.py'


class KEYS:
    IMPORTS = 'imports'
    NAME = 'name'
    TESTS = 'tests'
    TEST = 'test'
    STR = 'str'
    EXAMPLES = 'examples'
    FROM = 'from'
    EXPECT = 'expect'
    VARIABLES = 'variables'


class CONTENT:
    CLASS_CREATE_TEMPLATE = '\nclass Test{}{}(unittest.TestCase):\n'
    IMPORT_UNITTEST = 'import unittest\n'
    DEPS_IMPORT_TEMPLATE = 'from {} import {}\n'
    TEST_CASE_TEMPLATE = '    def test__{function_name}__{case_id}(self):'
    TESTERS_NOTES_TEMPLATE = '        {testers_notes}'
    VARIABLES_TEMPLATE = '        {variables}\n'
    ASSERTION_TEMPLATE = '        self.assertEqual({function}, {value})\n\n'


class PATTERNS:
    FUNCTION_CALL = r'example: [\s\S]+?(?=->)'
    IMPORT_DEC = '@need\n'
    VAR_DEC = r'@let '
    NEED_IMPORT = r'@need[\s\S]+?(?=@let|\d\))'
    NEEDED_VARIABLES = r'@let[\s\S]+?(?=\d\))'
    NUMBER_BULLET = r'\d\) '
    TEST_CASE_EXAMPLE = r'\d\) [\s\S]+?(?=\n)'
    EXAMPLE_PASSAGE = r'-{3,}[\s\S]+?(?=---)'
    TEST_SEP = ' -> '
