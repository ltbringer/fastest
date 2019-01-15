import argparse
import os
import time
import subprocess

from fastest.io.read_file import read_file
from fastest.code_assets.function import get_functions
from fastest.compiler import compile_tests
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', required=True, help='Project root, use $(pwd) to be sure')
parser.add_argument('--source',required=False, help='Modules to check coverage for')
parser.add_argument('--watch', help='Comma separated names of folders that should be watched')
parser.add_argument('--exclude', help='Comma separated names of folders that should NOT be watched')
args = parser.parse_args()


def main():
    print('Monitoring started...')

    if not os.path.exists('./test'):
        os.mkdir('./test')

    report_path = os.path.abspath(os.path.join(args.path, 'htmlcov/index.html'))

    class PyFileHandler(PatternMatchingEventHandler):
        patterns = ["*.py"]

        def process(self, event):
            """
            event.event_type
                'modified' | 'created' | 'moved' | 'deleted'
            event.is_directory
                True | False
            event.src_path
                path/to/observed/file
            """

            print(event.src_path, event.event_type)

            test_files = [
                test_file.replace('.py', '')
                for test_file in os.listdir('./test') if test_file not in ['__init__c', '__pycache__']
            ]

            print(test_files)

            if '__test.py' not in event.src_path and \
                    os.path.isfile(event.src_path):
                page = read_file(args.path, event.src_path)
                functions = get_functions(page)
                compile_tests.build(functions, event.src_path, args.path)

                command = ['test.{}'.format(test_file) for test_file in test_files]
                if (args.source):
                    subprocess.call(['coverage', 'run', '--source', args.source, '-m', 'unittest'] + command)
                else:
                    subprocess.call(['coverage', 'run', '-m', 'unittest'] + command)
                subprocess.call(['coverage', 'report'])
                subprocess.call(['coverage', 'html'])
                print(report_path)

        def on_modified(self, event):
            self.process(event)

        def on_created(self, event):
            self.process(event)

    observer = Observer()
    observer.schedule(PyFileHandler(), args.path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
