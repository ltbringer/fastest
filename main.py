import argparse
import os
import time
import subprocess

from core.io.read_file import read_file
from core.code_assets.function import get_functions
from core.compiler import compile
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler



parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', help='Project root, use $(pwd) to be sure')
args = parser.parse_args()


test_files = [
            test_file.replace('.py', '')
            for test_file in os.listdir('./test')
            if '__' not in test_file[:2]
        ]

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

        if '__test.py' not in event.src_path and \
                os.path.isfile(event.src_path) and \
                'core' not in event.src_path:
            page = read_file(args.path, event.src_path)
            functions = get_functions(page)
            compile.build(functions, event.src_path, args.path)

            command = ['test.{}'.format(test_file) for test_file in test_files]
            subprocess.call(['coverage', 'run', '--source', 'mocks', '-m', 'unittest'] + command)
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
