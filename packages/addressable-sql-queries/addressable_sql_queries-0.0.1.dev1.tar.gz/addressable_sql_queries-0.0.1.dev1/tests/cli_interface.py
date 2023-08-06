"""
Doctest for testing the preprocessor mode using the command line interface.
>>> perform_test()
 -- % clef_ici
SELECT 3;
<BLANKLINE>
SELECT 1;
<BLANKLINE>
 -- % b  
SELECT 5;
<BLANKLINE>
<BLANKLINE>
1 yields :
    SELECT 1;
<BLANKLINE>
2 yields :
     -- % clef_ici
SELECT 3;
<BLANKLINE>
3 yields :
     -- % clef_ici
SELECT 3;
<BLANKLINE>
4 yields :
     -- % a
SELECT 4;
SELECT "ho";
<BLANKLINE>
>>>
"""

from os.path import join
from os import getcwd
import sys

sys.path.append(join(getcwd(), "src", "addressable_sql_queries"))



def perform_test():
    from subprocess import run
    from shutil import copyfile
    from os import mkdir
    try:
        mkdir("tests/tests_temp_files")
    except FileExistsError:
        pass
    copyfile("tests/_target.sql", "tests/tests_temp_files/_target.sql")
    from os import environ
    sp_env = environ.copy()
    sp_env["PYTHONPATH"] = join(getcwd(), "src")
    run(["python", "-m", "src.addressable_sql_queries",
        "tests/tests_temp_files/_target.sql"], env=sp_env)
    from tests.tests_temp_files._target__sql_out import queries
    print(queries[1])
    print(queries[None])
    print(queries["b  "])
    print()
    [print(f"{i} yields :\n    ", queries.having_line(i), sep="")
     for i in range(1, 5)]
    from shutil import rmtree
    try:
        rmtree("tests/tests_temp_files")
    except FileNotFoundError:
        pass
