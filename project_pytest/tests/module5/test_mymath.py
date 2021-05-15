import pytest
import sys,os
sys.path.append(os.getcwd())

from src.mymath import *


@pytest.fixture(scope='function')
def initi():
    obj = Transform()
    yield obj


@pytest.mark.parametrize("in_put,out_put", [
    ('factorial;5', 120),
    ('factorial;[1,2,3]', [1, 2, 6]),
    ("factorial;{'a':1,'b':2,'c':3}", {'a': 1, 'b': 2, 'c': 6}),
    ('cube;5', 125), ('cube;[1,2,3]', [1, 8, 27]),
    ("cube;{'a':1,'b':2,'c':3}", {'a': 1, 'b': 8, 'c': 27}),
    ('square;5', 25),
    ('square;[1,2,3]', [1, 4, 9]),
    ("square;{'a':1,'b':2,'c':3}", {'a': 1, 'b': 4, 'c': 9})
])
def test_operations(initi, in_put, out_put):
    in_put1 = in_put.split(';')[0]
    in_put2 = in_put.split(';')[1]
    op = initi.execute(in_put1, eval(in_put2))
    assert op == out_put
