import argparse
import os
import fnmatch
import time
import subprocess

from fastest.io.read_file import read_file
from fastest.code_assets.function import get_functions
from fastest.compiler import compile_tests
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from logger.logger import logger


parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', help='Project root, use $(pwd) to be sure')
parser.add_argument('--source', help='Modules to check coverage for')
parser.add_argument('--poll-duration', default='1', help='Modules to check coverage for')
parser.add_argument(
    '--exclude',
    help='Comma separated names of files/dirs that should NOT be watched',
)

args = parser.parse_args()
monitor_path = args.path if args.path is not None else os.getcwd()
poll_duration = int(args.poll_duration) \
    if type(args.poll_duration) is str and \
    args.poll_duration.isdigit() \
    else 1


def make_test_module():
    if os.path.exists('./test'):
        return

    os.mkdir('./test')
    open('./test/__init__.py', 'a').close()

def get_report_path():
    return os.path.abspath(os.path.join(monitor_path, 'htmlcov/index.html'))


def get_test_files():
    test_files = os.listdir('./test')
    return [
        test_file.replace('.py', '')
        for test_file in test_files
        if '.pyc' not in test_file and
           '__pycache__' not in test_file
    ]


def is_path_to_be_ignored(event_path, ignore_patterns):
    for ignored_pattern in ignore_patterns:
        _, current_file_path = event_path.split(monitor_path + '/')
        if fnmatch.fnmatch(current_file_path, ignored_pattern):
            return True
    return False


def create_test_command():
    test_files = get_test_files()
    return ['test.{}'.format(test_file) for test_file in test_files]


def execute_coverage_and_tests(source):
    command = create_test_command()
    report_path = get_report_path()
    source_present_command = ['coverage', 'run', '--source', source, '-m', 'unittest'] + command
    source_missing_command = ['coverage', 'run', '-m', 'unittest'] + command
    subprocess.call(source_present_command) if source else subprocess.call(source_missing_command)
    subprocess.call(['coverage', 'report'])
    subprocess.call(['coverage', 'html'])
    logger.info('Check coverage: ' + report_path)


def main():
    logger.info('Monitoring started...')

    class PyFileHandler(PatternMatchingEventHandler):
        patterns = ['*.py']
        exclude_files = args.exclude if args.exclude is not None else ''
        ignore_patterns = [path.strip() for path in exclude_files.split(',')]
        ignore_patterns += ['test/*', '__pycache__', '*.pyc', '*__test.py']

        def process(self, event):
            if is_path_to_be_ignored(event.src_path, self.ignore_patterns):
                return None

            page = read_file(monitor_path, event.src_path)
            functions = get_functions(page)
            compile_tests.build(functions, event.src_path, monitor_path)
            execute_coverage_and_tests(args.source)

        def on_modified(self, event):
            self.process(event)

        def on_created(self, event):
            self.process(event)

    observer = Observer()
    observer.schedule(PyFileHandler(), monitor_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(poll_duration)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
