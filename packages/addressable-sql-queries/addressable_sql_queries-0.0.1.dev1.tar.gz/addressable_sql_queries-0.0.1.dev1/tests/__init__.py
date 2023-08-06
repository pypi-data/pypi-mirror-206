"""Convert all doctests to unittests."""


from tests import main


def load_tests(_loader, tests, _ignore):
    from doctest import DocTestSuite
    from tests import cli_interface, parser_mode_py_interface, preprocessor_mode_py_interface, init, newline
    from shutil import rmtree
    from unittest import FunctionTestCase

    def clean_dir():
        try:
            rmtree("tests/tests_temp_files")
        except FileNotFoundError:
            pass
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(cli_interface))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(parser_mode_py_interface))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(preprocessor_mode_py_interface))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(main))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(init))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    tests.addTest(DocTestSuite(newline))
    tests.addTest(FunctionTestCase(lambda: True, tearDown=clean_dir))
    return tests
