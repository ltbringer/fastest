import subprocess
from fastest.file_handler import test_command


def execute_tests(source):
    """
    Runs all tests within the tests directory
    :param source: str
    :return: None
    """
    subprocess.call(test_command(source))
