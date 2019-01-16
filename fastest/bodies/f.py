import uuid
from fastest.constants import KEYS, CONTENT
from fastest import code_style
from fastest.bodies.testers_notes import get_testers_notes


def case_generator():
    return str(uuid.uuid4()).upper().replace("-", "")[0:10]


def create_naive_test_case(function_object, test):
    test_template = CONTENT.TEST_CASE_TEMPLATE.format(
        function_name=function_object[KEYS.NAME],
        case_id=case_generator(),
    )

    if function_object[KEYS.TESTS][KEYS.VARIABLES]:
        for variable in function_object[KEYS.TESTS][KEYS.VARIABLES]:
            test_template += CONTENT.VARIABLES_TEMPLATE.format(variables=variable)

    test_template += CONTENT.ASSERTION_TEMPLATE.format(function=test[KEYS.FROM], value=test[KEYS.EXPECT])

    return test_template
