import os
import time


from fastest.file_handler.read_file import read_file
from fastest.code_assets.function import get_functions
from fastest.test_compiler import test_writer
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from fastest.logger.logger import logger
from fastest.cli.args import cli_args
from fastest.file_handler import make_test_module, execute_coverage, \
    execute_tests, is_path_to_be_ignored


monitor_path = cli_args.path if cli_args.path is not None else os.getcwd()

poll_duration = int(cli_args.poll_duration) \
    if type(cli_args.poll_duration) is str and \
    cli_args.poll_duration.isdigit() \
    else 1

make_test_module()


def main():
    logger.info('Monitoring started...')

    class PyFileHandler(PatternMatchingEventHandler):
        patterns = ['*.py']
        exclude_files = cli_args.exclude if cli_args.exclude is not None else ''
        ignore_patterns = [path.strip() for path in exclude_files.split(',')]
        ignore_patterns += ['test/*', '__pycache__', '*.pyc', '*__test.py']

        def process(self, event):
            if is_path_to_be_ignored(event.src_path, monitor_path, self.ignore_patterns):
                return None

            page = read_file(monitor_path, event.src_path)
            functions = get_functions(page)
            test_writer.build(functions, event.src_path, monitor_path)
            execute_tests(monitor_path)
            execute_coverage(monitor_path)

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
