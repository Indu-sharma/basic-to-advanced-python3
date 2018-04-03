import math
import pytest
from operations_python_objects import Transform


def square(in_put):
    if isinstance(in_put,(int,float,long)):
        value = in_put * in_put

    elif isinstance(in_put,list):
        value = [i * i for i in in_put]

    elif isinstance(in_put,dict):
        value = {k: in_put[k] * in_put[k] for k in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def cube(in_put):
    if isinstance(in_put,(int,float,long)):
        value = in_put * in_put * in_put
    elif isinstance(in_put,list):
        value = [i * i * i for i in in_put]
    elif isinstance(in_put,dict):
        value = {k: in_put[k] * in_put[k] * in_put[k] for k in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def factorial(in_put):
    if isinstance(in_put,(int,float,long)):
        value = math.factorial(in_put)

    elif isinstance(in_put,list):
        value = [math.factorial(i) for i in in_put]

    elif isinstance(in_put,dict):
        value = {key: math.factorial(in_put[key]) for key in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


class Transform:
    def __init__(self):
        pass

    def execute(self,method,params):
        return eval(method)(params)
    


@pytest.fixture(scope='function')
def initi():
    obj = Transform()
    return obj

@pytest.mark.parametrize("in_put,out_put", [
    ('factorial;5',120),
    ('factorial;[1,2,3]',[1,2,6]),
    ("factorial;{'a':1,'b':2,'c':3}",{'a': 1,'b': 2,'c': 6}),

    ('cube;5',125),('cube;[1,2,3]',[1,8,27]),
    ("cube;{'a':1,'b':2,'c':3}",{'a': 1,'b': 8,'c': 27}),

    ('square;5',25),
    ('square;[1,2,3]',[1,4,9]),
    ("square;{'a':1,'b':2,'c':3}",{'a': 1,'b': 4,'c': 9})
])
def test_operations(initi,in_put,out_put):
    in_put1 = in_put.split(';')[0]
    in_put2 = in_put.split(';')[1]
    op = initi.execute(in_put1,eval(in_put2))
    assert op==out_put
