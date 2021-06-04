# How to make PyPI Package

Description how to make PyPI pip installable package.

## Additions to Python Code

1. Create `__init__.py` and add there:
    * `__version__`
    * Import library functions
1. Create `setup.py` as in the example file

## Upload to PyPI

Instructions from [https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#testing-and-publishing-package-on-pypi](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#testing-and-publishing-package-on-pypi)

1. Register account on PYPI: [https://pypi.python.org](https://pypi.python.org)
1. Register test account on testpypi: [https://testpypi.python.org](https://testpypi.python.org)
1. Install needed libraries: `pip install wheel twine`
1. Build your library: `python setup.py bdist_wheel --universal`
1. Test how will it look in TestPyPI: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
1. Upload final working version to PyPI: `twine upload dist/*`

Now it is possible to use `pip install <library>`.

## Update Existing Library

1. Update version of the library in `__init__.py`
2. Run 3 last steps in the upper table
