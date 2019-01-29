import subprocess
import os
import pathlib
from fastest.logger.logger import logger


def execute_coverage(report_path):
    """
    Function with a side-effect to create
    coverage report and prints to stdout
    :param report_path: str
    :return: None
    """
    subprocess.call(['coverage', 'report'])
    subprocess.call(['coverage', 'html'])
    coverage_path = os.path.join(report_path, 'htmlcov', 'index.html')
    logger.info(pathlib.Path(coverage_path).as_uri())
