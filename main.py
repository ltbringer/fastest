import argparse
import os
import time

from core.io.read_file import read_file, get_current_directory
from core.code_assets.function import get_functions
from core.compiler import compile
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler



parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', help='Project root, use $(pwd) to be sure')
args = parser.parse_args()



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

        if '__test.py' not in event.src_path and os.path.isfile(event.src_path):
            page = read_file(args.path, event.src_path)
            functions = get_functions(page)
            compile.build(functions, event.src_path, args.path)

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
