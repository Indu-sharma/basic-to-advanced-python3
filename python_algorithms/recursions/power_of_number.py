"""
Problem - Calculate power of a number using recursion

Flow:
2**5 = 2 * 2**4
a**b = a * a**(b-1)

Base Case:
b == 0: return 1 || b == 1: return a
"""


def Pow(a, b):
    assert -1 < b == int(b), 'Invalid Power'
    assert int(a) == a, 'Invalid Base'
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * Pow(a, b - 1)


tests = [(1, 10), (10, 99), (0, -1), (10, 20),]
for test in tests:
    try:
        res = Pow(*test)
    except (TypeError, AssertionError) as e:
        print(f'Pow{test}= {e}')
    else:
        print(f'Pow{test} = {res}')
