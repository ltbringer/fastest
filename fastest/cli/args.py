import argparse


parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', help='Project root, use $(pwd) to be sure')
parser.add_argument('--source', help='Modules to check coverage for')
parser.add_argument('--poll-duration', default='1', help='Modules to check coverage for')
parser.add_argument(
    '--exclude',
    help='Comma separated names of files/dirs that should NOT be watched',
)

cli_args = parser.parse_args()
