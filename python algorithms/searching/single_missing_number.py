"""
Q. Given an Un-ordered List of Integers from  1 to n , Find a missing number.

There are various ways to solve this problem. Such as:
1. Using Iterative approach to check every elements in given list to range(1,n+1).
2. Using Hashing technique: Keep default value to zero for every elements of range(1,n+1).
Then update value of key for elements in given list to 1. At the end, any key having Zero value is the missing
element. This solution works for any number of missing  elements. 
3. XoR of two same number(or even number of same digits) is always Zero.
So using this logic: XOR of range(1,n+1) &  given list produces missing number.
4. Get the sum of elements in the list and sum of the n natural number : n(n+1)/2 ;
Take the difference to find a missing number.

Let's see all of them in practice.
"""

import random

"""
Generate a list with 50 as missing number and shuffle the list so that array is un-sorted.
We consider the first 100 natural numbers as the range to find missing number from.
"""
my_list = list(range(1, 50)) + list(range(51, 101))
random.shuffle(my_list)


def missing1(my_list):
    complete_list = range(1, 101)
    for i in complete_list:
        if i not in my_list:
            print(f'Missing Number is :{i}')


missing1(my_list)


def missing2(my_list):
    complete_list = range(1, 101)
    # Assign Zero value to every Keys. 
    my_dict = dict.fromkeys(complete_list, 0)
    for i in my_list:
        my_dict[i] = 1
    for key in my_dict:
        if my_dict[key] == 0:
            print(f'Missing Number is: {key}')


missing2(my_list)


def missing3(my_list):
    complete_list = list(range(1, 101))
    xor = my_list[0]
    for i in my_list[1:] + complete_list:
        xor = xor ^ i
    print(f'Missing Number is: {xor}')


missing3(my_list)


def missing4(my_list):
    n = 100
    total_sum = n * (n + 1) // 2
    sum_of_list = sum(my_list)
    missing_number = total_sum - sum_of_list
    print(f'Missing_number is: {missing_number}')


missing4(my_list)
