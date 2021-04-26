"""
Append and Remove : Memory Allocation
"""
import sys

a = [10, 11, 13, 14, 15, 18, 19] # 72 + 8*7
print(sys.getsizeof(a))
a.append(10)
print(sys.getsizeof(a))


a = [10, 11, 13, 14, 15, 18, 19]
print(sys.getsizeof(a))
a.remove(10)
print(sys.getsizeof(a)) #
a.insert(0,20)
print(sys.getsizeof(a))

import time
# Time Complexity of Append.

# O(1)
t1 = time.time()
a.append(10)
t2 = time.time()
print(t2-t1)


# O(N)
t1 = time.time()
a.insert(0,10)
t2 = time.time()
print(t2-t1)

# O(1)
t1 = time.time()
print(a[1])
t2 = time.time()
print(t2-t1)


"""
Convert following program to List Comprehension.  
"""
my_list = [[5,6,7],[7,8,9]]
out_list = []
for i in my_list:
    out_list.extend(i[::-1])
print(out_list)

# List Comprehension Solution
print([i for j in my_list for i in j[::-1]])





"""
Flatten the list with nested list reversed:

I/P - [10, [1,2,3],[5,6,7],[7,8,9]]
O/p - [10, 3,2,1,7,6,5,9,8,7]

Constraints:
- Solution should only contain 1 line. Hint: Use List comprehensions 
- Input has at Max Single Nesting.
- Time Complexity should be O(N)

"""
my_list = [10, [1, 2, 3], [5, 6, 7], [7, 8, 9]]
print([i for i in my_list if not isinstance(i, list)] + [i for j in my_list if isinstance(j, list) for i in j[::-1]])
