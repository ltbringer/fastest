import os


def get_report_path(project_path):
    """
    Returns the path to coverage report

    :param project_path: str
    :return: str
    """
    return os.path.abspath(os.path.join(project_path, 'htmlcov/index.html'))
