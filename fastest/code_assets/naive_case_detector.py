import re
from fastest.constants import KEYS, PATTERNS


FUNCTION_CALL = 0
OUTPUT = 1


def stack_imports(import_statements):
    return [
        import_statement.strip() + '\n'
        for import_statement in import_statements
        if len(import_statement) > 0
    ]


def stack_variables(variable_string):
    if type(variable_string) is not str:
        return ''
    variables = [
        variable.strip()
        for variable in variable_string.split(PATTERNS.VAR_DEC)
    ]
    return variables


def get_imports_from_docstring(example_passage):
    needed_imports = re.findall(PATTERNS.NEED_IMPORT, example_passage, re.M)
    needed_imports = needed_imports if len(needed_imports) > 0 else None
    if needed_imports is None:
        return []
    needed_imports = ''.join(needed_imports).replace(PATTERNS.IMPORT_DEC, '').split('\n')
    return stack_imports(needed_imports)


def get_variables_from_docstring(example_passage):
    needed_variables = re.findall(r'@let[\s\S]+?(?=\d\))', example_passage)
    needed_variables = needed_variables if len(needed_variables) > 0 else []
    return stack_variables(''.join(needed_variables))


def stack_examples(examples_strings):
    example_stack = []
    for example in examples_strings:
        test_function, expectation = re.sub(PATTERNS.NUMBER_BULLET, '', example, 1).split(PATTERNS.TEST_SEP)

        example_stack.append({
            KEYS.FROM: test_function,
            KEYS.EXPECT: expectation
        })
    return example_stack


def get_test_case_examples(example_passage):
    examples_strings = re.findall(PATTERNS.TEST_CASE_EXAMPLE, example_passage, re.M)
    examples_strings = examples_strings if len(examples_strings) > 0 else None
    return stack_examples(examples_strings)


def get_test_from_example_passage(statements):
    example_passage = re.findall(PATTERNS.EXAMPLE_PASSAGE, statements, re.I)
    example_passage = example_passage[0] if len(example_passage) > 0 else None
    if example_passage is None:
        return None
    import_statements = get_imports_from_docstring(example_passage)
    variables = get_variables_from_docstring(example_passage)
    examples = get_test_case_examples(example_passage)
    return None \
        if examples is None \
        else {
            KEYS.IMPORTS: import_statements,
            KEYS.VARIABLES: variables,
            KEYS.EXAMPLES: examples
        }
