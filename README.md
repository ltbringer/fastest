# Fastest
Creates unit tests from examples in the docstring and more (Currently supporting unix based systems only)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ae01d1185a9b4e93be06e6faf894448d)](https://app.codacy.com/app/AmreshVenugopal/fastest?utm_source=github.com&utm_medium=referral&utm_content=AmreshVenugopal/fastest&utm_campaign=Badge_Grade_Dashboard)
[![Scrutinizer_Badge](https://scrutinizer-ci.com/g/AmreshVenugopal/fastest/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/AmreshVenugopal/fastest/)
[![Build_Status](https://travis-ci.org/AmreshVenugopal/fastest.svg?branch=master)](https://travis-ci.org/AmreshVenugopal/fastest)
[![Coverage Status](https://coveralls.io/repos/github/AmreshVenugopal/fastest/badge.svg?branch=master)](https://coveralls.io/github/AmreshVenugopal/fastest?branch=master)
[![Current_Version](https://img.shields.io/pypi/v/fastest.svg)](https://pypi.org/project/fastest/)
[![Python_Version](https://img.shields.io/pypi/pyversions/fastest.svg)](https://pypi.org/project/fastest/)

## Install

```bash
$ pip install fastest
```

## Usage
```bash
$ fastest --path=$(pwd)
```
watches all .py files and creates coverage for entire project.

```bash
$ fastest --path=$(pwd) --source=py_module
```
where `path` is the the project root, and [`source`](https://coverage.readthedocs.io/en/coverage-4.3.4/source.html#source) 
is same as the value passed to the command `coverage run -m unittest --source=$source test`

```bash
$ fastest --path=$(pwd) --exclude=dont_check_this_dir/*,these__*.py
```
To exclude files/folders use `--exclude` and the file watcher will ignore them.
The `test/*` folder that `faster` creates is excluded by default.

## Introduction
Things that happen when you run `python main.py --path=$(pwd)`:

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
    ----
    examples:
    1) add(3, 4) -> 7 #
    """
    return x + y
```

 This will create a unittest in the `test` directory, `assertEqual(add(3, 4), 7)`
 within `Class test_<file>_<function>(self)` 
 (for the given directory, tree: `Class test_utils_add(self)`)

 4. Runs all tests that are created.
 5. Creates a coverage report (in html format).
 6. Print the link to the coverage reports' index.html.

## How to make best use of Fastest
 1. Keep your `functions` light:
    - Be paranoid about separation of concerns.
    - Too many conditions are a hint that you might need another function.
    - Complex loops and `if-else` are not scalable code, a single mistake would 
    take that tower down and feature additions would involve someone going through 
    that brain-teaser.
 2. Use libraries but wrap them with your own functions. Like: Use `requests` or the inevitable database? 
    wrap them with your own functions.
    - Helps with adding customizations in one place (configuring things like base url, and similar configs)
    - Helps mocking so that entire code-base can be unit tested.
 3. Docstrings may get outdated if your work pace is fast enough to 
    maintain quality documentation, but adding examples now would help you create 
    tests which prevents your descriptions from going stale, **either the tests fail 
    AND the description is outdated OR else everything is fine**.

## Fun facts
 1. Fastest uses itself for its nearly automated tests and documentation.
 2. Excluding the files that are to be changed infrequently, Fastest has 100% code coverage.
 3. Fastest has 2/32 test cases failing, a testimony to its ability to find bugs.


## Patch 11 updates:
 1. Allows creation of variables within the docstrings, which includes lambda functions!
 ```python
def quick_maths(a, b):
    """
    ----
    examples:
    @let a = {
        'apples': 3,
        'oranges': 4
    }
    
    1) quick_maths(a['apples'], a['oranges']) -> 7
    ----
    """
    return a + b
 ```
 2. Can include installed modules external to your project.
 ```python
def aint_nobody_got(time_fo_dat):
    """
    ---
    examples:
    @need
    from datetime import datetime
    1) aint_nobody_got(time_fo_dat) -> datetime.now()
    """
 ```
 3.  Can hence, include modules from your project. 
 Make sure that you use absolute import format.
 