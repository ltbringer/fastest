import subprocess
from logger.logger import logger


def execute_coverage(report_path):
    """
    Function with a side-effect to create
    coverage report and prints to stdout
    :param report_path: str
    :return: None
    """
    subprocess.call(['coverage', 'report'])
    subprocess.call(['coverage', 'html'])
    logger.info('Check coverage: ' + report_path)
