import os



def get_current_directory():
    return os.path.dirname(os.path.realpath(__file__))


def read_file(directory):
    goal_dir = os.path.join(os.getcwd(), "./test_fodder/main.py")
    with open(os.path.abspath(goal_dir), 'r') as fp:
        contents = fp.read()

    return contents, os.path.abspath(goal_dir)
