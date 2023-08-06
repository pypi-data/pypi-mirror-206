"""
>>> prepare_regular()
>>> test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql"])
SELECT 1;
<BLANKLINE>
>>> test_direct_access_existing("clef_ici", "_target")
Traceback (most recent call last):
    ...
AttributeError: module 'tests.tests_temp_files._target__sql_out' has no attribute 'clef_ici'
>>> clean_regular()
>>> test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql", "b", "-o"])
Traceback (most recent call last):
    ...
AssertionError: A -o doesn't have target file.
>>> test_with_arguments([sys.argv[0], "-o", "tests/tests_temp_files/_target.sql", "b"])
Traceback (most recent call last):
    ...
AssertionError: A -o doesn't have source file.
>>> test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql", "tests/tests_temp_files/_target.sql", "-o", "b", "-o", "c"])
Traceback (most recent call last):
    ...
AssertionError: Every -o should be preceded by a source file and followed by the target file to write to. Any parameter can only have one of these roles.
>>> test_with_arguments([sys.argv[0], "b", "-o", "c"])
Traceback (most recent call last):
    ...
AssertionError: One of the provided input files doesn't exist or isn't valid/readable.
>>> test_with_arguments(sys.argv[:1])
Traceback (most recent call last):
    ...
AssertionError: Please provide at least a source file.
>>> test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql", "tests/tests_temp_files/_target.sql", "-o", "-o", "c"])
Traceback (most recent call last):
    ...
AssertionError: Every -o should have a source file and a target file to write to.
>>> test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql", "-o", "a", "tests/tests_temp_files/_target.sql", "-o", "c"])
Traceback (most recent call last):
    ...
AssertionError: One of the provided input files doesn't exist or isn't valid/readable.
>>> tnwop = prepare_regular("tests/direct_access_ok.sql")
>>> test_with_arguments([sys.argv[0], tnwop])
SELECT 1;
<BLANKLINE>
>>> test_direct_access_existing("clef_ici", "direct_access_ok")
' -- % clef_ici\\nSELECT 3;\\n'
>>> clean_regular()
>>>
>>>
>>>
>>> tnwop2 = prepare_regular("tests/_target_no_trailing_whitespace_and_other.sql")
>>> test_with_arguments([sys.argv[0], tnwop2])
SELECT 1;
<BLANKLINE>
>>> test_direct_access_existing("clef_ici", "_target_no_trailing_whitespace_and_other")
Traceback (most recent call last):
    ...
AttributeError: module 'tests.tests_temp_files._target_no_trailing_whitespace_and_other__sql_out' has no attribute 'clef_ici'
>>> clean_regular()
>>>
>>>
>>>
>>> tnwop3 = prepare_regular("tests/already_in_python_basis_attr.sql")
>>> test_with_arguments([sys.argv[0], tnwop3])
SELECT 1;
<BLANKLINE>
>>> test_direct_access_existing("clef_ici", "already_in_python_basis_attr")
Traceback (most recent call last):
    ...
AttributeError: module 'tests.tests_temp_files.already_in_python_basis_attr__sql_out' has no attribute 'clef_ici'
>>> clean_regular()
"""
from src.addressable_sql_queries import __main__
import logging
import sys
from os import getcwd
from os.path import join


sys.path.append(join(getcwd(), "src"))



def test_direct_access_existing(i: int | str | None, module_name):
    from types import ModuleType
    from importlib import import_module as im
    out: ModuleType = im(f".{module_name}__sql_out", "tests.tests_temp_files")
    return getattr(out, i)


def test_with_arguments(argv: list[str], i: int | str | None = 0, ret = False):
    if len(argv) == 1 or any(e in ["-?", "--?", "-h", "--h", "-help", "--help"] for e in argv[1:]):
        print(
            """Usage : python -m addressable_queries input.sql [-o output.sql.out.py]. Multiple input (and optionnally outputs) can be passed. Can't change token or language with cli, use python api instead.""")
    preprocessing_tasks: dict[str,
                              str] = __main__.check_and_clean_entries(argv[1:])
    logging.info(repr(preprocessing_tasks))
    __main__.main(preprocessing_tasks)

    if ret:
        return
    
    from tests.tests_temp_files import _target__sql_out as out
    print(out.queries[i])


def prepare_regular(srcp: str = None) -> str:
    from shutil import copyfile
    from os import mkdir
    from os.path import join, basename, dirname
    try:
        mkdir("tests/tests_temp_files")
    except FileExistsError:
        pass
    src = "tests/_target.sql" if srcp is None else srcp
    dest = join(dirname(src), "tests_temp_files", basename(src))
    copyfile(src, dest)
    return dest if srcp is not None else None


def clean_regular():
    from shutil import rmtree
    try:
        rmtree("tests/tests_temp_files")
    except FileNotFoundError:
        pass


def perform_test():
    prepare_regular()
    test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql"])
    clean_regular()
    try:
        test_with_arguments(
            [sys.argv[0], "tests/tests_temp_files/_target.sql", "b", "-o"])
    except AssertionError:
        pass
    else:
        raise Exception("Bad input should have raised an exception.")
    try:
        test_with_arguments(
            [sys.argv[0], "-o", "tests/tests_temp_files/_target.sql", "b"])
    except AssertionError:
        pass
    else:
        raise Exception("Bad input should have raised an exception.")
    try:
        test_with_arguments([sys.argv[0], "tests/tests_temp_files/_target.sql",
                            "tests/tests_temp_files/_target.sql", "-o", "b", "-o", "c"])
    except AssertionError:
        pass
    else:
        raise Exception("Bad input should have raised an exception.")
    try:
        test_with_arguments([sys.argv[0], "b", "-o", "c"])
    except AssertionError:
        pass
    else:
        raise Exception("Bad input should have raised an exception.")

