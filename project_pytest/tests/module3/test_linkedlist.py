
def test_iter(createlinklists):
    a, b = createlinklists
    IsIterable = 'False'
    try:
        for i in a:
            pass
        IsIterable = 'True'
    except:
        IsIterable = 'False'
    assert IsIterable == 'True'


def test_eq(createlinklists):
    a, b = createlinklists
    assert a == b


def test_str(createlinklists):
    a, b = createlinklists
    assert a == [4, 3, 2, 1, 1]


def test_repr(createlinklists):
    a, b = createlinklists
    assert repr(a) == "'LinkedList([4, 3, 2, 1, 1])'"


def test_substraction(createlinklists):
    a, b = createlinklists
    assert a - b == [0, 0, 0, 0, 0]


def test_multiplication(createlinklists):
    a, b = createlinklists
    assert a * b == [16, 9, 4, 1, 1]


def test_addition(createlinklists):
    a, b = createlinklists
    assert a + b == [8, 6, 4, 2, 2]


def test_len(createlinklists):
    a, b = createlinklists
    assert len(a) == 5