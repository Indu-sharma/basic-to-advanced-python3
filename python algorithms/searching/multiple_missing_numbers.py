"""
Q. Given an Un-ordered List of Integers from  1 to n , Find two missing number.
There are various ways to solve this problem. Such as:
1. Using Iterative approach to check every elements in given list to range(1,n+1).
Refer to single_missing_number.py
2. Using Hashing technique: Keep default value to zero for every elements of range(1,n+1).
Then update value of key for elements in given list to 1. At the end, any key having Zero value is the missing
element. This solution works for any number of missing  elements.
Refer to single_missing_number.py
3. XoR of two same number(or even number of same digits) is always Zero.
So using this logic: XOR of range(1,n+1) &  given list produces a missing number.
For two numbers once, we get XOR of two missing numbers; we need to XOR all such numbers where
rightmost bit is set to 1.
4. Get the sum of elements in the list and sum of the n natural number : n(n+1)/2 ;
x + y = n(n+1)/2 - sum(all elements in list)
x * y = n!/Multiply(all elements in list)
And x = (x+y) - (x*y)
Let's see all of them in practice.
"""
import random
from math import factorial as f
import numpy as np
from functools import reduce

"""
Generate a list with 51 & 1 as missing number and shuffle the list so that array is un-sorted.
We consider the first 100 natural numbers as the range to find missing number from.

"""
my_list = list(range(2, 51)) + list(range(52, 101))
random.shuffle(my_list)


def missing3(my_list):
    complete_list = list(range(1, 101))
    xor = my_list[0]
    x = y = 0
    # This gives x XOR y  
    for i in my_list[1:] + complete_list:
        xor = xor ^ i
    right_set_bit = xor & ~(xor - 1)  # 1's complement gives the difference of x & y bit.
    for i in my_list + complete_list:
        if i & right_set_bit:
            x = x ^ i
        else:
            y = y ^ i

    print(f'Two missing numbers are : {x}, {y}')


missing3(my_list)


def missing4(my_list):
    n = 100
    mul_list = reduce(lambda x, y: x * y, my_list)
    x_mul_y = f(n) // mul_list
    x_add_y = n * (n + 1) // 2 - sum(my_list)
    """
    Substituting x from x_add_y to x*y=x_mul_y, gives us polynomial equation : 
    x**2 - x_add_y * x + x_mul_y = 0
    Now, Lets solve this polynomial equation using numpy module.
    """
    coef = [1, -x_add_y, x_mul_y]
    x = np.roots(coef)  # Gives the two possible values of x.
    print(f'Two missing numbers are: {int(x[0])}, {int(x[1])}')


missing4(my_list)
