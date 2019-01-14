import uuid
from fastest.type import type_inference
from fastest import code_style
from fastest.bodies.testers_notes import get_testers_notes


def case_generator():
    return str(uuid.uuid4()).upper().replace("-", "")[0:10]


def create_var_type_test_case(function_obj, variable_name, statements):
    function_name = function_obj['name']
    args = ', '.join(function_obj['args'])
    expected_types = type_inference.infer(variable_name, statements)
    if len(expected_types) == 1:
        expected_type = expected_types[0]
        type_message = 'Automatically detected type of {variable} to be an {type}'\
            .format(variable=variable_name, type=expected_type)
        return """
    def test__{function}__for_typeof__arg__{variable}(self):
        # You must always check type of arguments 
        # to prevent unexpected crashes
        #
        # Feel free to remove this test if you're confident that this is not required
    
        # {message}
        
        self.assert({function}({args}), {type})
        
""".format(function=function_name, args=args, variable=variable_name, message=type_message, type=expected_type)
    else:
        expected_type = ''
    return """
    def test__{function}__for_typeof__arg__{variable}(self):
        # You must always check type of arguments 
        # to prevent unexpected crashes
        #
        # Feel free to remove this test if you're confident that this is not required
        
        
        self.assert({function}({args}), {type})
    
""".format(function=function_name, args=args, variable=variable_name, type=expected_type)


def create_return_type_test_case(function_obj, return_values, statements):
    function_name = function_obj['name']
    args = ', '.join(function_obj['args'])
    for return_value in return_values:
        expected_types = type_inference.infer(return_value, statements)
        multi_type_return = len(list(set(expected_types))) > 1
        if multi_type_return:
            type_message = 'Seems like the return value {} is one of {}. ' \
                           'Be very careful with such functions, ' \
                           'a better approach would be to have different ' \
                           'functions to perform the different kind of tasks'.format(return_value, expected_types)
            expected_type = ''

            return """
    def test__{function}__for_typeof_return__{variable}(self):
        # You must always have checkpoints for return values 
        #
        # Feel free to remove this test if you're confident that this is not required
    
        # {message}
        self.assertIs({function}({args}), {type})
        
""".format(function=function_name, args=args, variable=return_value, message=type_message, type=expected_type)

        else:
            expected_type = expected_types[0]
            return """
    def test__{function}__for_typeof_return__{variable}(self):
        # You must always have checkpoints for return values 
        #
        #
        # Feel free to remove this test if you're confident that this is not required
    
        self.assertIs({function}({args}), {type})
        
""".format(function=function_name, args=args, variable=return_value, type=expected_type)


def create_naive_test_case(function_object, test):
    function_too_long = code_style.is_function_too_long(function_object['str'])
    has_too_many_conditions = code_style.has_too_many_if_statements(function_object['str'])
    control_structure_overuse = code_style.get_loop_complexity(function_object['str'])

    testers_notes = get_testers_notes(function_too_long, has_too_many_conditions, control_structure_overuse)

    return """
    def test__{function_name}__{case_id}(self):
        {testers_notes}
        self.assertEqual({function}, {value})
    """.format(
        function_name=function_object['name'],
        case_id=case_generator(),
        function=test['from'],
        value=test['expect'],
        testers_notes=testers_notes
    )
