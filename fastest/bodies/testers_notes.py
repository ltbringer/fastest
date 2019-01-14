def on_depth(depth):
    return """
    # testers notes:
    # --------------
    # Your function has {depth} lines of code, it is strongly advised to break them
    # when they are doing too many operations.
    """.format(depth=depth)


def on_conditional_complexity(condition_complexity):
    return """
    # testers notes:
    # --------------
    # Your function has {condition_complexity} conditions, it is strongly advised to convert them
    # to individual functions. It is likely that they are doing different tasks.
    """.format(condition_complexity=condition_complexity)


def on_control_overuse(control_overuse):
    return """
    # testers notes:
    # --------------
    # Your function has {control_overuse} number of nested loops!!
    # please try to find a better way, there has to be one.
    """.format(control_overuse=control_overuse)


def get_testers_notes(depth, condition_complexity, control_overuse):
    function_too_deep, lines = depth
    complex_conditions, complexity = condition_complexity
    control_overuse, nested_loops = control_overuse
    notes = ''

    if function_too_deep:
        notes += on_depth(lines) + '\n\n'
    if complex_conditions:
        notes += on_conditional_complexity(complexity) + '\n\n'
    if control_overuse:
        notes += on_control_overuse(nested_loops) + '\n\n'
    return notes
