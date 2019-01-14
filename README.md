## Fastest
Creates unit tests from examples in the docstring and more


### Install

```
$ pip install fastest
```

### Usage
```
$ python main.py --path=$(pwd) --source=<source>
```
where `path` is the the project root, and [`source`](https://coverage.readthedocs.io/en/coverage-4.3.4/source.html#source) 
is same as the value passed to the command `coverage run -m unittest --source=$source test`


### Introduction
Things that happen when you run `python main.py --path=$(pwd) --source=<source>` in your
python project:

1. Checks for a `test` file at the project root, it creates if it doesn't find one.
2. Watches `.py` files for changes.
3. Creates unittests if a function has examples in its docstrings like so:

```python
# .
# ├──module_a
# ├──module_b
#    └── utils.py
#
def add(x, y):
    """
    example: add(3, 4) -> 7 #
    """
    return x + y
```

This will create a unittest in the `test` directory, `assertEqual(add(3, 4), 7)`
within `Class test_<file>_<function>(self)` 
(for the given directory, tree: `Class test_utils_add(self)`)

4. Runs all tests that are created.
5. Creates a coverage report (in html format).
6. Print the link to the coverage reports' index.html.



