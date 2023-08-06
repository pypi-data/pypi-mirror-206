"""
Doctest for testing the parser mode using the python interface.
>>> perform_test()
 -- % a
SELECT 4;
SELECT "ho";
<BLANKLINE>
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
 -- % clef_ici
SELECT 3;
<BLANKLINE>
"""
from src.addressable_sql_queries import *


def perform_test():
    from shutil import copyfile
    from os import mkdir
    try:
        mkdir("tests/tests_temp_files")
    except FileExistsError:
        pass
    copyfile("tests/_target.sql", "tests/tests_temp_files/_target.sql")
    q1 = Query.fromFile("tests/tests_temp_files/_target.sql")
    print(q1.having_line(5))
    print(q1.having_line(4))
    print(q1[6])
    print(q1["b  "])
    with open("tests/tests_temp_files/_target.sql") as fi:
        q2 = Query.fromFile(fi)
    print(q2.having_line(3))
    try:
        Query.fromFile("tests/_target_dup_err.sql")
    except ValueError:
        pass
    else:
        raise Exception(
            "Duplicate key in parsed file didn't trigger error (they should have).")
    from shutil import rmtree
    try:
        rmtree("tests/tests_temp_files")
    except FileNotFoundError:
        pass
