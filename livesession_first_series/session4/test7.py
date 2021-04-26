"""
Today's Goal:
1. List Internals:
- Memory Storage, Copy, Shallow Copy & Deep Copy
- Memory Allocations on Append/Remove
- Time Complexity Of the List Operations(Traverse/Random Access/Search/Append/Insert).
2. List Comprehensions
3. Solve a Problem using List Comprehension.
"""

import sys
import copy

a = ['10', [5, 6], 11]
b = copy.deepcopy(a)

print(id(a), id(a[0]), id(a[1]))
print(sys.getsizeof(a), sys.getsizeof(a[0]), sys.getsizeof(a[1]), sys.getsizeof(a[2])) # 72+28*2


print(id(b), id(b[0]), id(b[1]))  # 72+28*2
print(sys.getsizeof(b), sys.getsizeof(b[0]), sys.getsizeof(b[1]))  # 72+28*2


b[1][0] = 50
print('After Modification of b:\n')

print(id(a), id(a[0]), id(a[1]))  # 72+28*2
print(list(map(sys.getsizeof, [a, a[0], a[1]])))  # 72+28*2

print(id(b),id(b[0]), id(b[1]))  # 72+28*2
print(list(map(sys.getsizeof, [b, b[0], b[1]])))  # 72+28*2

print(a, b)