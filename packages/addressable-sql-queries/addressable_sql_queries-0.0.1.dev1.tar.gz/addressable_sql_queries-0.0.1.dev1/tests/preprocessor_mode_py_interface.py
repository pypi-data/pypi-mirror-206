"""
Doctest for testing the preprocessor mode using the python interface.
>>> perform_test()
 -- % a
SELECT 4;
SELECT "ho";
<BLANKLINE>
 -- % 9876132
SELECT 8;
<BLANKLINE>
 -- % b  
SELECT 5;
<BLANKLINE>
preprocess_to_str('')='no_query_available = "input file was likely empty"'
"""


def perform_test():
    from shutil import copyfile
    from os import mkdir
    try:
        mkdir("tests/tests_temp_files")
    except FileExistsError:
        pass
    copyfile("tests/_target.sql", "tests/tests_temp_files/_target.sql")
    from src.addressable_sql_queries import preprocess_to_str
    with open("tests/tests_temp_files/_target.sql") as fi:
        s = fi.read()
    with open("tests/tests_temp_files/preprocessed1_sql_out.py", "w") as fo:
        fo.write(preprocess_to_str(s))
    from tests.tests_temp_files.preprocessed1_sql_out import queries as q1
    print(q1.having_line(5))
    print(q1[6])
    print(q1["b  "])
    print(f"{preprocess_to_str('')=}")
    from src.addressable_sql_queries import _python_builtin_factory
    try:
        _python_builtin_factory([" ", ""], [0], [None])
    except ValueError:
        pass
    else:
        raise Exception(
            "Lists (as python_builtin_factory arguments) with different length didn't trigger error (they should have).")
    from shutil import rmtree
    try:
        rmtree("tests/tests_temp_files")
    except FileNotFoundError:
        pass
