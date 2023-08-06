"""
>>> type(f("_target_no_end_nl_1.sql", False))
<class 'src.addressable_sql_queries.Query'>
>>> f("_target_no_end_nl_1.sql", False)[None] == f("_target_no_end_nl_1.sql", False)[0]
True
>>> f("_target_no_end_nl_1.sql", False)[0][:3] == "SEL"
True
>>> f("_target_no_end_nl_1.sql", False)[-1][-9:]
'SELECT 8;'
>>> f("_target_no_end_nl_1.sql", True)[-1][-9:]
'SELECT 8;'
>>> f("_target_no_end_nl_1.sql", False)[-1][4:10]
'% kk98'
>>> f("_target_no_end_nl_1.sql", True)[-1][4:10]
'% kk98'
>>> f("_target_no_end_nl_2.sql", False)[-1][-5:]
'22222'
>>> f("_target_no_end_nl_2.sql", True)[-1]
' -- % 98761322222'
>>> f("_target_empty.sql", True)
Traceback (most recent call last):
    ...
KeyError: 'queries'
>>> f("_target_empty.sql", True, True)["no_query_available"]
'input file was likely empty'
>>> f("_target_empty.sql", False)[0] == ""
True
>>> f("_target_empty.sql", False)[1]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>>
>>> f("_target_no_newline1.sql", True)[2]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> f("_target_no_newline1.sql", True)[-1][-2:]
'_1'
>>> f("_target_no_newline1.sql", False)[0]
''
>>> f("_target_no_newline1.sql", True).having_line(1)
' -- % just_one_key_1'
>>> f("_target_no_newline1.sql", False).having_line(1)
' -- % just_one_key_1'
>>> f("_target_no_newline1.sql", False)[1]
' -- % just_one_key_1'
>>> f("_target_no_newline2.sql", False)[0]
'SELECT 2 / 2;'
>>> f("_target_no_newline2.sql", False)[-1]
'SELECT 2 / 2;'
>>> f("_target_no_newline2.sql", False)[1]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> round(eval(f("_target_no_newline2.sql", False)[None][7:-1]))
1
>>> len(f("_target_no_newline2.sql", True)[None])
13
>>>
>>> # Keys tests
>>> f("_target_empty.sql", False)[None][-6:]
''
>>> f("_target_no_newline1.sql", True)["just_one_key_1"][-6:]
'_key_1'
>>> round(eval(f'22{f("_target_no_newline2.sql", True)[0][-6:-1]}'))
111
>>> f("_target_no_newline1.sql", False)["just_one_key_1"][-6:]
'_key_1'
>>>
>>> # Having line tests
>>> f("_target_empty.sql", False).having_line(4200)[-6:]
''
>>> f("_target_no_newline1.sql", True).having_line(0)[-6:]
Traceback (most recent call last):
    ...
AssertionError: The value has no element lower or equal to it.
>>> f("_target_no_newline2.sql", True).having_line(1)[-6:]
'2 / 2;'
>>> f("_target_no_newline1.sql", False).having_line(4200)[-6:]
'_key_1'
"""
from os.path import join
from os import getcwd
import sys


sys.path.append(join(getcwd(), "src"))

from src.addressable_sql_queries import Query, preprocess_to_str


def f(fn: str, pp: bool, jd: bool = False):
    fn = join("./tests", fn)
    if pp:
        with open(fn) as fi:
            d = {}
            s = preprocess_to_str(fi.read())
            exec(s, d, d)
            if jd:
                return d
            return d["queries"]
    else:
        return Query.fromFile(fn)


def perform_test():
    raise NotImplementedError()
    type(f("_target_no_end_nl_1.sql", False))
    f("_target_no_end_nl_1.sql", False)[None] == f("_target_no_end_nl_1.sql", False)[0]
    f("_target_no_end_nl_1.sql", False)[0][:3] == "SEL"
    f("_target_no_end_nl_1.sql", False)[-1][-9:]
    f("_target_no_end_nl_1.sql", True)[-1][-9:]
    f("_target_no_end_nl_1.sql", False)[-1][4:10]
    f("_target_no_end_nl_1.sql", True)[-1][4:10]
    f("_target_no_end_nl_2.sql", False)[-1][-5:]
    f("_target_no_end_nl_2.sql", True)[-1]
    f("_target_empty.sql", True)
    f("_target_empty.sql", True, True)["no_query_available"]
    f("_target_empty.sql", False)[0] == ""
    f("_target_empty.sql", False)[1]
    f("_target_no_newline1.sql", True)[2]
    f("_target_no_newline1.sql", True)[-1][-2:]
    f("_target_no_newline1.sql", False)[0]
    f("_target_no_newline1.sql", False)[1]
    f("_target_no_newline2.sql", False)[0]
    f("_target_no_newline2.sql", False)[-1]
    f("_target_no_newline2.sql", False)[1]
    round(eval(f("_target_no_newline2.sql", False)[None][7:-1]))
    len(f("_target_no_newline2.sql", True)[None])
        # Keys tests
    f("_target_empty.sql", False)[None][-6:]
    f("_target_no_newline1.sql", True)["just_one_key_1"][-6:]
    round(eval(f'22{f("_target_no_newline2.sql", True)[0][-6:-1]}'))
    f("_target_no_newline1.sql", False)["just_one_key_1"][-6:]
        # Having line tests
    f("_target_empty.sql", False).having_line(4200)[-6:]
    f("_target_no_newline1.sql", True).having_line(0)[-6:]
    f("_target_no_newline2.sql", True).having_line(1)[-6:]
    f("_target_no_newline1.sql", False).having_line(4200)[-6:]
    ...
