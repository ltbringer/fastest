import re
from fastest.code_assets import keywords


def get_variables(statements, arguments):
    statements = statements.split('\n')
    statements = statements[1:]
    statements = ' '.join(statements)
    statements = re.sub(r'\s+', ' ', statements).replace(':', '')
    words = statements.split(' ')
    exclude_options = keywords.RESERVED + arguments
    return list(set([word for word in words if word not in exclude_options and word.isalpha()]))
