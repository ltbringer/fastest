import os


def make_test_module():
    """
    A function with side-effect of creating a python module
    for containing tests at the root of a project.
    """
    if os.path.exists('./test'):
        return None
    # If there is a test module present
    # at the target location, exit.

    os.mkdir('./test')
    # If there is no `test` module, create one

    open('./test/__init__.py', 'a').close()
    # Create an __init__.py so that
    # the dir is identified as a python module
