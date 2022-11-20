# Secure Software Development (Computer Science)

The file `code_with_lint.py` was run against a variety of linters, i.e., `pylint`, `pyflakes`, `pycodestyle`, and `pydocstyle`, to test the quality of its associated code.

As per the screenshots provided as evidence under the folder `pictures_linters`:

1) Overall, `pylint` was found to be the most comprehensive linting tool, which included all qualitative findings reported by each of the other three linters individually, and it also returned a quantitative score as a measure of code quality.
2) `pyflakes` only considered imports and the usage of local variables. 
3) `pycodestyle` solely evaluated the code style, as per the PEP-8 standards.
4) `pydocstyle` assessed whether the docstrings were present and suggested cosmetic changes to apply in them when required.
