"""
Command line interface
"""
from . import preprocess_to_str
import logging


def main(files: dict[str, str]) -> None:
    for output_path, source_path in files.items():
        with open(source_path) as source_file:
            input = source_file.read()
        result = preprocess_to_str(input)
        with open(output_path, "w") as output_file:
            output_file.write(result)

def check_and_clean_entries(arguments: list[str]) -> dict[str, str]:
    from os.path import isfile, dirname, basename, join
    if not (len(arguments) > 0): raise AssertionError("Please provide at least a source file.")
    if not (len(arguments) >= len([*filter(lambda e: e == "-o", arguments)]) * 3): raise AssertionError("Every -o should have a source file and a target file to write to.")
    o_indexes = [e[0]
                 for e in filter(lambda ie: ie[1] == "-o", enumerate(arguments))]
    logging.debug([(ind, arguments[ind]) for ind in o_indexes])
    if len(o_indexes):
        if not (max(o_indexes) < len(
            arguments) - 1): raise AssertionError("A -o doesn't have target file.")
        if not (min(o_indexes) > 0): raise AssertionError("A -o doesn't have source file.")
    for i1, i2 in zip(o_indexes[1:], o_indexes[:1]):
        if not (abs(i1 - i2) > 2): raise AssertionError("Every -o should be preceded by a source file and followed by the target file to write to. Any parameter can only have one of these roles.")
    working = {k: v for k, v in enumerate(arguments) if v != "-o"}
    source_output_dict = {}
    for co_i in o_indexes:
        source_output_dict[working.pop(co_i + 1)] = working.pop(co_i - 1)
    for auto_source in working.values():
        source_output_dict[join(dirname(auto_source), (basename(
            auto_source).replace(".", "__") + "_out.py"))] = auto_source
    if not (all(map(isfile, source_output_dict.values(
    )))): raise AssertionError("One of the provided input files doesn't exist or isn't valid/readable.")
    return source_output_dict


if __name__ == "__main__":
    from sys import argv
    if any(e in ["-?", "--?", "-h", "--h", "-help", "--help"] for e in argv[1:]):
        print(
            """Usage : python -m addressable_queries input.sql [-o output.sql.out.py]. Cant change token or language with cli, use python api instead for this purpose.""")
        exit(0)
    preprocessing_tasks: dict[str, str] = check_and_clean_entries(argv[1:])
    logging.info(repr(preprocessing_tasks))
    main(preprocessing_tasks)
