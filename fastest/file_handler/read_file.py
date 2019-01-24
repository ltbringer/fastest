import os


def read_file(dir_path, file_path):
    """
    Read contents of a .py file and return as text
    :param dir_path: str
    :param file_path: str
    :return: str
    """
    goal_dir = os.path.join(dir_path, file_path)
    with open(os.path.abspath(goal_dir), 'r') as fp:
        contents = fp.read()
    return contents
