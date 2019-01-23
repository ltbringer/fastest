import uuid
from fastest.constants import KEYS, CONTENT


def case_generator():
    """
    Use uuid to create test-case unique name
    :return:
    """
    return str(uuid.uuid4()).upper().replace("-", "")[0:10]


def get_empty_of_type(input_type):
    """
    Return an empty form of a given type
    :param input_type: str
    :return: str
    """
    empty_type = {
        'str': '\'\'',
        'int': '0',
        'list': '[]',
        'dict': '{}'
    }
    return empty_type[input_type]


def create_naive_test_case(function_object, test):
    """
    ----
    :param function_object:
    :param test:
    :return:
    """
    test_template = CONTENT.TEST_CASE_TEMPLATE.format(
        function_name=function_object[KEYS.NAME],
        case_id=case_generator(),
    )

    params = []
    for param in function_object[KEYS.TESTS][KEYS.PARAMS]:
        params.append(get_empty_of_type(param))

    if len(params) > 0:
        empty_param_call = '{}({})'.format(function_object[KEYS.NAME], ', '.join(params))

        test_template += CONTENT.TYPE_ASSERT_TEMPLATE.format(
            function=empty_param_call, value=function_object[KEYS.TESTS][KEYS.RETURN]
        )

    if function_object[KEYS.TESTS][KEYS.VARIABLES]:
        for variable in function_object[KEYS.TESTS][KEYS.VARIABLES]:
            test_template += CONTENT.VARIABLES_TEMPLATE.format(variables=variable)

    test_template += CONTENT.ASSERTION_TEMPLATE.format(function=test[KEYS.FROM], value=test[KEYS.EXPECT])
    return test_template
