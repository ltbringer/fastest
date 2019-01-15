import uuid
from fastest.constants import KEYS, CONTENT
from fastest import code_style
from fastest.bodies.testers_notes import get_testers_notes


def case_generator():
    return str(uuid.uuid4()).upper().replace("-", "")[0:10]


def create_naive_test_case(function_object, test):
    function_body               = function_object[KEYS.STR]
    function_too_long           = code_style.is_function_too_long(function_body)
    has_too_many_conditions     = code_style.has_too_many_if_statements(function_body)
    control_structure_overuse   = code_style.get_loop_complexity(function_body)
    testers_notes               = get_testers_notes(
        function_too_long,
        has_too_many_conditions,
        control_structure_overuse
    )

    test_template = CONTENT.TEST_CASE_TEMPLATE.format(
        function_name=function_object[KEYS.NAME],
        case_id=case_generator(),
    )

    if testers_notes:
        test_template += CONTENT.TESTERS_NOTES_TEMPLATE.format(testers_notes=testers_notes)

    if function_object[KEYS.TESTS][KEYS.VARIABLES]:
        for variable in function_object[KEYS.TESTS][KEYS.VARIABLES]:
            test_template += CONTENT.VARIABLES_TEMPLATE.format(variables=variable)

    test_template += CONTENT.ASSERTION_TEMPLATE.format(function=test[KEYS.FROM], value=test[KEYS.EXPECT])

    return test_template
