import os



def get_current_directory():
    return os.path.dirname(os.path.realpath(__file__))


def read_file(dir_path, file_path):
    goal_dir = os.path.join(dir_path, file_path)
    with open(os.path.abspath(goal_dir), 'r') as fp:
        contents = fp.read()

    return contents
