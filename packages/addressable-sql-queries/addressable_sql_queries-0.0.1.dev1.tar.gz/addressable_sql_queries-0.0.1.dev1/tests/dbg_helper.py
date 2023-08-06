from sys import path, argv
from os import path as op
from pathlib import Path


path += [str(Path(argv[0]).parent.parent.absolute())]

import tests.parser_mode_py_interface
import tests.preprocessor_mode_py_interface
import tests.cli_interface
import tests.main
import tests.init
import tests.newline


tests.cli_interface.perform_test()
print("$"*30)
tests.preprocessor_mode_py_interface.perform_test()
print("$"*30)
tests.parser_mode_py_interface.perform_test()
print("$"*30)
tests.main.perform_test()
print("$"*30)
tests.init.perform_test()
print("$"*30)
tests.newline.perform_test()
