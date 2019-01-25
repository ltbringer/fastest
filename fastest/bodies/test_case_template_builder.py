import uuid
from fastest.constants import Keys, Content


def case_generator(uuid_val=None):
    """
    ----
    examples:
    1) case_generator('a55eff11-ed51-ecb37-ccba') -> 'A55EFF11ED'
    ----
    Use uuid to create test-case unique name
    :return:
    """
    uuid_val = uuid_val if uuid_val is not None else str(uuid.uuid4())
    return str(uuid_val).upper().replace("-", "")[0:10]


def get_empty_of_type(input_type):
    """
    Return an empty form of a given type
    ----
    examples:

    1) get_empty_of_type('str') -> "''"
    2) get_empty_of_type('???') -> None
    ----
    :param input_type: str
    :return: str
    """
    empty_type = {
        'str': '\'\'',
        'int': '0',
        'list': '[]',
        'dict': '{}'
    }

    return empty_type.get(input_type)


def get_params_list(params):
    """
    ----
    examples:

    1) get_params_list(['str', 'str', 'list', 'dict']) -> ["''", "''", '[]', '{}']
    2) get_params_list(['str', '???']) -> ["''"]
    ----
    :param params: list
    :return: list
    """
    return [
        get_empty_of_type(param)
        for param in params
        if param in ['str', 'int', 'list', 'dict']
    ]


def create_type_test_case(function_object, params):
    """
    Create test case for checking types of function
    -----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    function_object = {
        'tests': {
            'return': 'str'
        },
        'name': 'function_1'
    }
    params = ['str', 'str']
    @end

    1) create_type_test_case(function_object, params) -> TestBodies.TYPE_TEST_CASE_1
    -----
    :param function_object: dict
    :param params: list
    :return: str
    """
    empty_param_call = '{}({})'.format(function_object.get(Keys.NAME), ', '.join(params))
    return Content.TYPE_ASSERT_TEMPLATE.format(
        function=empty_param_call, value=function_object.get(Keys.TESTS, {}).get(Keys.RETURN)
    )


def create_type_test_case_if_params(function_object, params):
    """
    Create type test case if there is info over params and return
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    function_object = {
        'tests': {
            'return': 'str'
        },
        'name': 'function_1'
    }

    params = ['str', 'str']
    @end

    1) create_type_test_case_if_params(function_object, params) -> TestBodies.TYPE_TEST_CASE_2
    ----
    :param function_object: dict
    :param params: list
    :return: str
    """
    return create_type_test_case(function_object, params)\
        if is_type_test_ready(function_object, params)\
        else ''


def is_type_test_ready(function_object, params):
    """
    if a function has params and return type specified, return True
    else False
    ----
    examples:

    @let
    function_object_1 = {
        'tests': {
            'return': 'str'
        }
    }

    function_object_2 = {'tests': {}}

    params = ['str', 'str']
    @end

    1) is_type_test_ready(function_object_1, params) -> True
    2) is_type_test_ready(function_object_2, params) -> False
    3) is_type_test_ready(function_object_1, []) -> False
    ----
    :param function_object: dict
    :param params: list
    :return: bool
    """
    return_type = function_object.get(Keys.TESTS, {}).get(Keys.RETURN)
    return bool(return_type and len(params) > 0)


def create_assertion_test(function_object):
    """
    Create assertion test cases by embedding into the template strings
    if examples are present in the docstrings
    -----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    function_object_1 = {
        'tests': {
            'variables': ['a = 5']
        }
    }

    function_object_2 = {'tests': {'variables': []}}

    params = ['str', 'str']
    @end

    1) create_assertion_test(function_object_1) -> TestBodies.ASSERTION_TEST_1
    2) create_assertion_test(function_object_2) -> ''
    -----
    :param function_object: dict
    :return: str
    """
    template = ''
    if function_object.get(Keys.TESTS, {}).get(Keys.VARIABLES):
        for variable in function_object.get(Keys.TESTS, {}).get(Keys.VARIABLES, []):
            template += Content.VARIABLES_TEMPLATE.format(variables=variable)
    return template


def create_naive_test_case(function_object, test, test_id=None):
    """
    Create test cases from the assertions, docstring params and return types
    ----
    examples:

    @need
    from fastest.constants import TestBodies
    @end

    @let
    function_object = {
        'tests': {
            'return': 'str',
            'variables': ['a = 5']
        },
        'name': 'function_1'
    }

    test = {
        'from': 'function_1',
        'expect': '2'
    }

    test_id = 'a55eff11-ed51-ecb37-ccba'
    @end

    1) create_naive_test_case(function_object, test, test_id) -> TestBodies.NAIVE_TEST_RESULT
    ----
    :param function_object: dict
    :param test: dict
    :param test_id: str
    :return: str
    """
    test_template = Content.TEST_CASE_TEMPLATE.format(
        function_name=function_object.get(Keys.NAME),
        case_id=case_generator(test_id),
    )

    params = get_params_list(function_object.get(Keys.TESTS, {}).get(Keys.PARAMS, []))

    test_template += create_type_test_case_if_params(function_object, params)
    test_template += create_assertion_test(function_object)
    test_template += Content.ASSERTION_TEMPLATE.format(function=test.get(Keys.FROM), value=test.get(Keys.EXPECT))
    return test_template
