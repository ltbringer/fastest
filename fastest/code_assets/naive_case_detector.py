import re


FUNCTION_CALL = 0
OUTPUT = 1


def get_naive_case(statements):
    """
    example: get_naive_case("example: fn_do_work() -> 8 #") -> [{
        "from": "fn_do_work()",
        "expect": 8
    }]
    #

    :param statements:
    :return:
    """
    function_call_pattern = r'example: [\s\S]+?(?=->)'
    total_pattern = r'example: [\s\S]+?(?=#)'
    function_call_matches = re.findall(function_call_pattern, statements, re.M)
    total_matches = re.findall(total_pattern, statements, re.M)

    test_cases = []

    for func_match, total_match in zip(function_call_matches, total_matches):
        func_match = func_match.replace('example:', '').strip()

        expectation = total_match\
          .replace(func_match, '')\
          .replace('example:', '')\
          .replace('->', '')\
          .strip()

        test_cases.append({
            'from': func_match,
            'expect': expectation
        })
    return test_cases