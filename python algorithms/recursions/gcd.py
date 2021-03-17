"""
Problem : Find the GCD of two numbers.

"""


def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(25, 8))
