"""
Example usage :
Import Query and create one with a filename (Query.fromFile), then access the parsed blocks with subscript [] using blocks index or keys, or .having_line method to get the block associated with a line. Default parameters are for SQL using python, and the delimiter is " -- % ", followed by the key that has to be unique for each chunk. First chunk has None as a key.
It is advised, when higher performances are needed, to use the "preprocessor" mode, and not the "parser mode" (using preprocess_to_str
 instead of Query, and then using the output file).
There is always at least one block, which starts at the beginning of the file, and might be empty. 
3 ways to use it are supported : preprocessor with cli (with python -m), preprocessor as python module, and parser as python module. Last two can be used simultaneously.
Potential flaw : delimiter appearing in a string litteral at the beginning of a line, for instance.
The following delimiter should prevent this for MySQL and SQLite :
 -- '" %% 
"""
from __future__ import annotations
import typing
import re
import warnings
import logging

LINE_COUNTING_OFFSET = 1

##############################
# PARSER MODE SPECIFIC
##############################


def _get_highest_lower_or_equal_index(container: list, value: typing.Any):
    """Get the index of the last element of the container lower or equal to value. Do not use with duplicate keys/elements."""
    if value in container:
        return container.index(value)
    container.append(value)
    container = sorted(container)
    ret = container.index(value) - 1
    if not (ret >= 0): raise AssertionError("The value has no element lower or equal to it.")
    return ret


class Query:
    def __init__(self, input_: str, delimiter: str | re.Pattern[str] = " -- % ") -> None:
        """Can be used with multiple files concatenated as str (in this case, make sure that the last query is followed by a ; at the end for SQL.)."""
        sql_chunks, first_line_indexes, keys = to_chunks(input_, delimiter)
        if not (len(sql_chunks) == len(first_line_indexes) == len(keys)): AssertionError("Input lists have different sizes.")
        for key in keys:
            if key is not None and re.search("[\t ]$", key):
                warnings.warn(
                    f"The key \"{key}\" has trailing whitespace. You might want to clean these, or to make sure to remind to put them to get this query.")
                break
        self.queries_first_lines = [
            n + LINE_COUNTING_OFFSET for n in first_line_indexes]
        self.queries_dict = dict(zip(keys, sql_chunks))

    @staticmethod
    def fromFile(filename: str | typing.IO, delimiter: str | re.Pattern[str] = " -- % ") -> Query:
        if isinstance(filename, str):
            with open(filename) as fi:
                input_ = fi.read()
        else:
            input_ = filename.read()
        return Query(input_, delimiter)

    def __getitem__(self, index: typing.Optional[str | int]) -> str:
        """Query instances are subscriptable, using str or None for the key, or an integer to get the nth chunk."""
        if isinstance(index, int):
            return self.queries_dict[list(self.queries_dict)[index]]
        else:
            return self.queries_dict[index]

    def having_line(self, line_number: int) -> str:
        """Get the chunk starting at a given line, or in general, having a given line."""
        if line_number == self.queries_first_lines[0] and self[None] == "" and len(self.queries_dict) > 1:
            return self[_get_highest_lower_or_equal_index(self.queries_first_lines, line_number) + 1]
        return self[_get_highest_lower_or_equal_index(self.queries_first_lines, line_number)]

##############################
# DEFAULT LANGUAGE FACTORY
##############################


def is_usable_id(s: str) -> bool:
    if not s.isidentifier():
        return False
    from addressable_sql_queries import default_python_basis # type: ignore
    if hasattr(default_python_basis, s):
        return False
    if s in [
        "queries_dict",
        "queries_first_lines",
    ]:
        return False
    return True

def _python_builtin_factory(sql_chunks: list[str], first_line_indexes: list[int], keys: list[typing.Optional[str]]) -> str:
    if not (len(sql_chunks) == len(first_line_indexes) == len(keys)):
        raise ValueError("Input lists have different sizes.")
    if not len(sql_chunks) or (len(sql_chunks) == 1 and not len(sql_chunks[0])):
        return "no_query_available = \"input file was likely empty\""
    for key in keys:
        if key is not None and re.search("[\\t ]$", key):
            warnings.warn(
                f"The key \"{key}\" has trailing whitespace. You might want to clean these, or to make sure to remind to put them to get this query.")

    first_line_indexes = [n + LINE_COUNTING_OFFSET for n in first_line_indexes]
    q_d = dict(zip(keys, sql_chunks))

    from os.path import dirname, join
    with open(join(dirname(__file__), "default_python_basis.py")) as fi:
        sour = fi.read()
    new = f"{sour}\n"\
        f"queries_first_lines = {repr(first_line_indexes)}\nqueries_dict = {repr(q_d)}"
    logging.debug(new)

    keys_s: list[str] = typing.cast(list[str], keys[1:])
    if all(map(is_usable_id, keys_s)):
        new += "\n" + "\n".join(map(lambda s: f"{s[1]} = {repr(sql_chunks[s[0] + 1])}", enumerate(keys_s))) + f"\n__all__ = [\"queries\", {', '.join([*map(lambda s: repr(s), keys_s), ''])}]\n"

    return new

##############################
# SHARED
##############################


@typing.overload
def to_chunks(input_: str, delimiter: str) -> tuple[list[str], list[int], list[typing.Optional[str]]]:
    """
    :param input_: is the str that will be processed into the three lists.
    :param delimiter: str will be escaped for usage with regular expressions, prepended with a ^
    appended with a line-wide wildcard capture group that will capture keys, and finished with a $.
    """
    ...


@typing.overload
def to_chunks(input_: str, delimiter: re.Pattern[str]) -> tuple[list[str], list[int], list[typing.Optional[str]]]:
    """
    :param input_: is the str that will be processed into the three lists.
    :param delimiter: pattern will be used as is, and should contain at least one group that will capture keys. First group will be used if multiple are available.
    """
    ...


def to_chunks(input_: str, delimiter: re.Pattern[str] | str) -> tuple[list[str], list[int], list[typing.Optional[str]]]:
    if isinstance(delimiter, str):
        delimiter = re.compile(f"^{re.escape(delimiter)}(.*)$", re.M)
    matches: list[typing.Match[str]] = [*re.finditer(delimiter, input_)]
    logging.debug(matches)
    pos: list[typing.Optional[int]] = [0]
    line_bounds = [0]
    for match in matches:
        pos.append(match.start(0))
        line_bounds.append(input_[:match.start(0)].count("\n"))
    pos.append(None)
    segments = []
    for bounds in zip(pos[:-1], pos[1:]):
        current_chunk = input_[bounds[0]:bounds[1]]
        segments.append(current_chunk)

    logging.debug(pos)
    logging.debug(segments)

    keys: list[typing.Optional[str]] = [None] + [e[1] for e in matches]

    if len(keys) != len(set(keys)):
        for dup_key_candidate in keys: # pragma: no branch
            if keys.count(dup_key_candidate) > 1:
                raise ValueError(
                    f"Keys must be unique. There was only {len(set(keys))} different keys out of {len(keys)} keys. Example of duplicate key : \"{dup_key_candidate}\".")
        raise RuntimeError()  # pragma: no cover

    return segments, line_bounds, keys


def preprocess_to_str(input_: str, delimiter: str | re.Pattern = " -- % ", factory = _python_builtin_factory) -> str:
    """
    With a given str, return a preprocessed str, which (if the factory is compliant) returns code (as str) that should be able to be used to get the nth chunk of the the input str, the chunk corresponding to a query, and the chunk having a given line (or starting at a given line).
    A delimiter, and a factory can be provided to overwrite defaults.
    The :param delimiter: can be the part that should precede the key on a line (containing nothing else than these two elements) if a str if given. Else it should be a re.Pattern that will be used, and every match will seperate two chunks ; it should have at least one group, and the first group (possibly the only one) will be the key.
    The :param factory: will be used to generate the output code from the chunks, the list of the first line number of each chunk, and the list of keys.
    """
    return factory(*to_chunks(input_, delimiter))


__all__ = [
    "preprocess_to_str",
    "Query",
]
