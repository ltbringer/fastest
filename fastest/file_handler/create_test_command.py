import os


def get_test_files():
    """
    Create a list of test files in the test directory
    excluding .pyc and __pycache__

    :return: list
    """
    test_files = os.listdir('./test')
    return [
        create_test_file_name(test_file)
        for test_file in test_files
        if is_valid_test_file(test_files)
    ]


def is_valid_test_file(test_file):
    """
    Checks if file is a .pyc or from __pycache__
    :param test_file: str
    :return: str
    """
    return '.pyc' not in test_file and '__pycache__' not in test_file


def create_test_file_name(test_file):
    """
    Append `test.` over file names to run all tests via `unittest`
    :param test_file: str
    :return: str
    """
    'test.{}'.format(test_file.replace('.py', ''))


def test_command(source):
    """
    Creates a command to be run via subprocess
    :param source: str|None
    :return: list
    """
    command = ['pytest', '--cov', source] if source is not None else ['pytest', '--cov']
    return command
