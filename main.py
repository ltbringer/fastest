import argparse
from core.io.read_file import read_file, get_current_directory
from core.code_assets.function import get_functions
from core.compiler import compile



page, path = read_file(get_current_directory())
functions = get_functions(page)

parser = argparse.ArgumentParser(description='Create test cases automatically')
parser.add_argument('--path', help='Project root, use $(pwd) to be sure')
args = parser.parse_args()
compile.build(functions, path, args.path)
