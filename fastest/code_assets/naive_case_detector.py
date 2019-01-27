import re
from fastest.constants import Keys, Patterns


FUNCTION_CALL = 0
OUTPUT = 1


def format_imports(import_statements):
    """
    -----
    examples:
    @need
    from fastest.constants import TestBodies
    @end

    @let
    input = TestBodies.TEST_STACK_IMPORTS_INPUT
    output = TestBodies.TEST_STACK_IMPORTS_OUTPUT
    @end
    1) format_imports(input) -> output
    -----
    :param import_statements: list
    :return: list
    """
    return [
        '{}\n'.format(import_statement.strip())
        for import_statement in import_statements
        if len(import_statement) > 0
    ]


def get_imports_from_docstring(example_passage):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    example_passage = TestBodies.EXAMPLE_WITH_IMPORTS
    import_statements = TestBodies.TEST_IMPORT_EXTRACTION
    empty_example_passage = ''
    @end

    1) get_imports_from_docstring(example_passage) -> import_statements
    1) get_imports_from_docstring(empty_example_passage) -> []
    ----
    :param example_passage: str
    :return: list
    """
    needed_imports = re.findall(Patterns.NEED_IMPORT, example_passage, re.M)
    needed_imports = needed_imports if len(needed_imports) > 0 else None
    if needed_imports is None:
        return []

    needed_imports = ''.join(needed_imports).replace(Patterns.IMPORT_DEC, '').split('\n')
    return format_imports(needed_imports)


def get_variables_from_docstring(example_passage):
    """
    ----
    examples:
    @need
    from fastest.constants import TestBodies
    @end

    @let
    example_passage = TestBodies.TEST_VARIABLES_FROM_DOCSTRING
    empty_example_passage = ''
    expected_output = TestBodies.TEST_VARIABLES_FROM_DOCSTRING_RESULT
    @end

    1) get_variables_from_docstring(empty_example_passage) -> ''
    2) get_variables_from_docstring(example_passage) -> expected_output
    ----
    :param example_passage: str
    :return: list
    """
    needed_variables = re.findall(Patterns.NEEDED_VARIABLES, example_passage)
    if len(needed_variables) == 0:
        return ''
    needed_variables = needed_variables[0]
    needed_variables = needed_variables.replace('@let', '')
    return needed_variables.split('\n')


def stack_examples(examples_strings):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    example_strings = TestBodies.STACK_EXAMPLES_TEST
    @end

    1) stack_examples('') -> []
    2) stack_examples(example_strings) -> [{'expect': '25', 'from': 'square(5)'}]
    ----
    :param examples_strings: list
    :return: list
    """
    example_stack = []
    try:
        for example in examples_strings:
            test_function, expectation = re.sub(Patterns.NUMBER_BULLET, '', example, 1)\
                .rsplit(Patterns.TEST_SEP, 1)

            example_stack.append({
                Keys.FROM: test_function,
                Keys.EXPECT: expectation
            })
        return example_stack
    except ValueError as ve:
        return []


def get_params_from_docstring(statements):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    statements = TestBodies.GET_PARAMS_FROM_DOCSTRING_TEST
    @end

    1) get_params_from_docstring('') -> []
    2) get_params_from_docstring(statements) -> TestBodies.EXPECT_PARAMS
    ----
    :param statements: str
    :return: list
    """
    params = re.findall(r':param .*:(.*)', statements)
    return [
        param.replace(' ', '')
        for param in params
    ]


def get_return_from_docstring(statements):
    """
    ----
    examples:
    @need
    from fastest.constants import TestBodies
    @end

    @let
    statements = TestBodies.RETURN_TYPE_TEST
    @end

    1) get_return_from_docstring('') -> None
    2) get_return_from_docstring(statements) -> 'int'
    ----
    :param statements: str
    :return: str
    """
    return_statement = re.search(r':return: (.*)', statements)
    return return_statement.group(1) if return_statement is not None else None


def get_test_case_examples(example_passage):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end


    @let
    example_passage = TestBodies.TEST_EXAMPLE_PASSAGE
    @end

    1) get_test_case_examples(example_passage) -> TestBodies.TEST_EXAMPLE_PASSAGE_RESULT
    ----
    :param example_passage: str
    :return: list
    """
    examples_strings = re.findall(Patterns.TEST_CASE_EXAMPLE, example_passage, re.M)
    examples_strings = examples_strings if len(examples_strings) > 0 else []
    return stack_examples(examples_strings)


def get_test_from_example_passage(statements):
    """
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    statements = TestBodies.NAIVE_CASE_TEST_STATEMENT
    @end

    1) get_test_from_example_passage(statements) -> TestBodies.NAIVE_CASE_TEST_RESULT
    2) get_test_from_example_passage(None) -> None
    3) get_test_from_example_passage('lorem ipsum') -> None
    ----
    :param statements:
    :return:
    """
    if statements is None:
        return None

    example_passage = re.findall(Patterns.EXAMPLE_PASSAGE, statements, re.I)
    example_passage = example_passage[0] if len(example_passage) > 0 else None
    if example_passage is None:
        return None
    import_statements = get_imports_from_docstring(example_passage)
    variables = get_variables_from_docstring(example_passage)
    examples = get_test_case_examples(example_passage)
    params = get_params_from_docstring(statements)
    return_statement = get_return_from_docstring(statements)

    return None \
        if examples is None \
        else {
            Keys.IMPORTS: import_statements,
            Keys.VARIABLES: variables,
            Keys.EXAMPLES: examples,
            Keys.PARAMS: params,
            Keys.RETURN: return_statement
        }
