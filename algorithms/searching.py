import inspect

"""
Linear Search complexity is O(n)
"""

my_arr = [1, 2, 3, 4, 6, 8, 9, 10]
search = 9


def linear_search(arr, x):
    for i in arr:
        if i == x:
            return f"{inspect.stack()[0][3]} : {x} is found in the array {arr} "
    return f"{inspect.stack()[0][3]} : {x} is not found in the array"


res = linear_search(my_arr, search)
print(res)

"""
Recursive  Binary Search Complexity O(log(n))

"""


def binary_recursive(arr, x):
    r = len(arr)
    m = len(arr) // 2

    if r <= 1:
        return -1

    if arr[m] == x:
        return m
    elif arr[m] > x:
        return binary_recursive(arr[:m], x)
    else:
        return binary_recursive(arr[m:], x)


res = binary_recursive(my_arr, search)
if res != -1:
    print(f"binary_recursive :  {search} is found in the array {my_arr}")
else:
    print(f"binary_recursive: {search} is not found in the array {my_arr}")

"""
Iterative  Binary Search Complexity O(log(n))

"""


def binary_iterative(arr, l, r, x):
    while l <= r:
        m = (l + r - 1) // 2
        if arr[m] == x:
            return m

        if arr[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1


res1 = binary_iterative(my_arr, 0, len(my_arr) - 1, search)
if res1 != -1:
    print(f"binary_iterative : {search} is found in the array {my_arr}")
else:
    print(f"binary_iterative: {search} is not found in the array {my_arr}")

"""
****** OUTPUT ********

linear_search : 9 is found in the array [1, 2, 3, 4, 6, 8, 9, 10] 
binary_recursive :  9 is found in the array [1, 2, 3, 4, 6, 8, 9, 10]
binary_iterative : 9 is found in the array [1, 2, 3, 4, 6, 8, 9, 10]
"""
