"""
>>> test_compiled_pattern()
False False
>>> warnings.simplefilter("error")
>>> warnings.warn("ensuring warning is on")
Traceback (most recent call last):
    ...
UserWarning: ensuring warning is on
>>> test_no_trailing_whitespace()
 -- % clef_ici
SELECT 3;
<BLANKLINE>
No trailing ws ok.
>>> raise_user_warning()
Traceback (most recent call last):
    ...
UserWarning: The key "b  " has trailing whitespace. You might want to clean these, or to make sure to remind to put them to get this query.
>>> _get_highest_lower_or_equal_index([*range(3, 10)], 2)
Traceback (most recent call last):
    ...
AssertionError: The value has no element lower or equal to it.
>>> warnings.simplefilter("default") # resetting warning simplefilter to default
>>> warnings.warn("This should be ok.")
"""
import warnings
from src.addressable_sql_queries import Query, to_chunks, _get_highest_lower_or_equal_index

warnings, _get_highest_lower_or_equal_index

def test_compiled_pattern():
    from re import compile
    with open("tests/_target.sql") as fi:
        inp = fi.read()
        p = compile("^(.*)$")
        r = to_chunks(inp, p)[0]
        r = "\n".join(r)
        print(r < inp, inp < r)


def test_no_trailing_whitespace():
    q = Query.fromFile(
        "tests/_target_no_trailing_whitespace_and_other.sql")
    print(q[1])
    print("No trailing ws ok.")


def raise_user_warning():
    Query.fromFile("tests/_target.sql")
    print("This should not be printed.")


def clean_regular():
    from shutil import rmtree
    try:
        rmtree("tests/tests_temp_files")
    except FileNotFoundError:
        pass


def perform_test():
    test_compiled_pattern()
    test_no_trailing_whitespace()
