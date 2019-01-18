import re
from fastest.constants import KEYS, PATTERNS


FUNCTION_CALL = 0
OUTPUT = 1


def stack_imports(import_statements):
    """
    -----
    examples:

    @let
    output = ['from datetime import datetime\\n', 'import numpy as np\\n']
    @end
    1) stack_imports(['from datetime import datetime  ', ' import numpy as np ']) -> output
    -----
    :param import_statements:
    :return:
    """
    return [
        import_statement.strip() + '\n'
        for import_statement in import_statements
        if len(import_statement) > 0
    ]

def get_imports_from_docstring(example_passage):
    """
    ----
    examples:

    @let
    no_import_in_docstring = 'nothing to see here'
    docstring_with_imports = 'import numpy as np'
    @end

    1) get_imports_from_docstring(no_import_in_docstring) -> []
    2) get_imports_from_docstring(docstring_with_imports) -> []
    ----
    :param example_passage:
    :return:
    """
    needed_imports = re.findall(PATTERNS.NEED_IMPORT, example_passage, re.M)
    needed_imports = needed_imports if len(needed_imports) > 0 else None
    if needed_imports is None:
        return []
    needed_imports = ''.join(needed_imports).replace(PATTERNS.IMPORT_DEC, '').split('\n')
    return stack_imports(needed_imports)


def get_variables_from_docstring(example_passage):
    """
    ----
    examples:
    1) get_variables_from_docstring("@let\\na = 1\\n@end") -> ['a = 1']
    ----

    :param example_passage:
    :return:
    """
    needed_variables = re.findall(PATTERNS.NEEDED_VARIABLES, example_passage)
    if len(needed_variables) == 0:
        return ''
    needed_variables = needed_variables[0]
    needed_variables = needed_variables.replace('@let', '')
    return needed_variables.split('\n')


def stack_examples(examples_strings):
    """
    -----
    examples:

    @let
    output = [{
        'from': 'stack_examples("1) some_fn() -> 1")',
        'expect': 1
    }]
    @end
    1) stack_examples([]) -> []
    2) stack_examples("1) some_fn() -> 1") -> output
    -----
    :param examples_strings:
    :return:
    """
    example_stack = []
    for example in examples_strings:
        test_function, expectation = re.sub(PATTERNS.NUMBER_BULLET, '', example, 1)\
            .rsplit(PATTERNS.TEST_SEP, 1)

        example_stack.append({
            KEYS.FROM: test_function,
            KEYS.EXPECT: expectation
        })
    return example_stack



def get_params_from_docstring(statements):
    params = re.findall(r':param .*:(.*)', statements, re.M)
    return [
        param.replace(' ', '')
        for param in params
    ]


def get_return_from_docstring(statements):
    return_statement = re.search(r':return: (.*)', statements, re.M)
    return return_statement.group(1) if return_statement is not None else None


def get_test_case_examples(example_passage):
    """
    ----
    examples:

    @let
    example_passage = '1) some_fn() -> 1'
    output = [{
        'from': 'stack_examples("1) some_fn() -> 1")',
        'expect': 1
    }]
    @end
    1) get_test_case_examples(example_passage) -> output
    ----
    :param example_passage:
    :return:
    """
    examples_strings = re.findall(PATTERNS.TEST_CASE_EXAMPLE, example_passage, re.M)
    examples_strings = examples_strings if len(examples_strings) > 0 else []
    return stack_examples(examples_strings)


def get_test_from_example_passage(statements):
    """
    ----
    examples:

    @let
    some_fn = lambda: 1
    output = {
        'imports': ['import numpy as np']
        'variables': ['a = 1'],
        'examples': [{
            'from': 'some_fn()',
            'expect': 1
        }]
    }
    @end

    1) get_test_from_example_passage('---\\n@needs\\nimport numpy as np\\n@end\\n\\n@let\\na = 1\\n1) some_fn() -> 1') -> output
    ----
    :param statements:
    :return:
    """
    if statements is None:
        return None

    example_passage = re.findall(PATTERNS.EXAMPLE_PASSAGE, statements, re.I)
    example_passage = example_passage[0] if len(example_passage) > 0 else None
    if example_passage is None:
        return None
    import_statements = get_imports_from_docstring(example_passage)
    variables = get_variables_from_docstring(example_passage)
    examples = get_test_case_examples(example_passage)
    params = get_params_from_docstring(statements)
    return_statement = get_return_from_docstring(statements)
    print('params', params)
    print('return', return_statement)
    return None \
        if examples is None \
        else {
            KEYS.IMPORTS: import_statements,
            KEYS.VARIABLES: variables,
            KEYS.EXAMPLES: examples,
            KEYS.PARAMS: params,
            KEYS.RETURN: return_statement
        }
