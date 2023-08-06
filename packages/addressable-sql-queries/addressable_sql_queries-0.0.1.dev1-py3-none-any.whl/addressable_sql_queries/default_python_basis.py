"""
Automatically adapted module containing addressable chunks of SQL. Import queries from this module and use [] or .having_line on it.
If all the keys are compatible with it, they will be turned into identifiers associated directly with the query, and importable by from xxx import *
Note that if you do so with multiple preprocessed scripts, the variable queries and possibly the variables named from the keys of the source scripts will collide.
"""
import typing
queries_dict: dict[typing.Optional[str], str]
queries_first_lines: list[int]


def _get_highest_lower_or_equal_index(container: list, value: typing.Any):
    """Get the index of the last element of the container lower or equal to value. Do not use with duplicate keys/elements."""
    if value in container:
        return container.index(value)
    container.append(value)
    container = sorted(container)
    ret = container.index(value) - 1
    if not (ret >= 0): raise AssertionError("The value has no element lower or equal to it.")
    return ret


class _QueriesType:
    def __getitem__(self, index: typing.Optional[str | int]) -> str:
        """Get the nth chunk using an integer, or the chunk associated with a key, using str or None."""
        if isinstance(index, int):
            return queries_dict[list(queries_dict)[index]]
        else:
            return queries_dict[index]

    def having_line(self, line_number: int) -> str:
        """Get the chunk starting at a given line, or in general, having a given line."""
        if line_number == queries_first_lines[0] and queries[None] == "" and len(queries_dict) > 1:
            return queries[_get_highest_lower_or_equal_index(queries_first_lines, line_number) + 1]
        return queries[_get_highest_lower_or_equal_index(queries_first_lines, line_number)]


queries = _QueriesType()
