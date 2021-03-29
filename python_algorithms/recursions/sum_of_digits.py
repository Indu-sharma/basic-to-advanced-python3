"""
Problem - Find the sum of the digits of an integer

131 :: 131 % 10 + Sum(131 // 10)
Recursion Function(n):: n % 10 + Sum(n // 10)
Base Case :: 0<=n<10 , return n
Unintentional Case :: 0 <= n == int(n)
Recursive Calls:
    1st pass: 1 + Sum(13)
    2nd pass: 1 + 3 + Sum(1)
    3rd pass: 1 + 3 + 1 = 5
"""


def Sum(n):
    assert 0 <= n == int(n), 'The Input is either non-integer or negative'
    if n in range(0, 10):
        return n
    return n % 10 + Sum(n // 10)


tests = [-1, 0, 9, 80 ,9999, 200, 'x', 9.16, 1.111111]
for test in tests:
    try:
        res = Sum(test)
    except (AssertionError, TypeError) as e:
        print(f"Invalid Input : {test}")
    else:
        print(f'Input: {test}, Output: {res}')
