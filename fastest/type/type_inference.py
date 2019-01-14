from fastest.type import type_usage_patterns


INT         = 0
STR         = 1
LIST        = 2
TUPLE       = 3
DICT        = 4
type_map    = ['int', 'str', 'list', 'tuple', 'dict']


def infer(variable, statements):
    """
    example: infer("list_var", "def fn():\n\tlist_var = [1]") -> ['list'] #
    example: infer("some_var", "def fn():\n\tsome_var + some_other") -> ['int', 'str'] #
    :param variable:
    :param statements:
    :return:
    """
    statements = statements.split('\n')
    statements = statements[1:]
    type_chances = [0] * 5
    for statement in statements:
        type_chances[INT]   += type_usage_patterns.used_as_int(statement, variable)
        type_chances[STR]   += type_usage_patterns.used_as_str(statement, variable)
        type_chances[LIST]  += type_usage_patterns.used_as_list(statement, variable)
        type_chances[TUPLE] += type_usage_patterns.used_as_tuple(statement, variable)
        type_chances[DICT]  += type_usage_patterns.used_as_dict(statement, variable)

    max_prob_type = max(type_chances)
    if type_chances.count(max_prob_type) > 1:
        return [type_map[i] for i, type_chance in enumerate(type_chances) if type_chance == max_prob_type]
    else:
        return [type_map[type_chances.index(max_prob_type)]]
