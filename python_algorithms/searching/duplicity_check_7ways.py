# Problem : Find the duplicate elements or check duplicity in the array.

"""
Solution-1: Naive solution using nested loop.
Time Complexity: O(n^2) , Space Complexity : O(n)

"""
print('*******Solution - 1*********')
my_list = [5, 4, 1, 2, 3, 5]
print('Duplicate Elements :')
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] == my_list[j]:
            print(my_list[i])


"""
Solution-2: Keep track of visited list.
Time Complexity: Better than O(n^2) in most cases, Space Complexity : O(n)
"""

print('**********Solution - 2**********')
my_list = [5, 4, 1, 2, 3, 5]
visited = []
for i in my_list:
    if i not in visited:
        visited.append(i)
    else:
        print(i)
"""
Solution-3: Use Counter module
Time Complexity: O(n), Space Complexity : O(n)
"""
print('********Solution - 3**********')
from collections import Counter

my_list = [5, 4, 1, 2, 3, 5]
c = Counter(my_list)
for k in c:
    if c[k] > 1:
        print(k)

"""
Solution-4: Using Set 
Time Complexity: O(n), Space Complexity : O(n)
Constraints: 
1. It only checks if the duplicate elements exist.  
"""
print('*******Solution - 4********')
my_list = [5, 4, 1, 2, 3, 5]
my_set = set(my_list)

if len(my_set) < len(my_list):
    pass
else:
    print('No Duplicate')

for i in my_set:
    count = my_list.count(i)
    if count > 1:
        print(f'{ i } is repeated { count } times')

"""
Solution-5 : Using Sorting 
Time Complexity : O(nLogN) , Space Complexity: O(1)
"""
print('********Solution - 5**********')
my_list = [5, 4, 1, 2, 3, 5]
my_list.sort()
prev = my_list[0]
for i in my_list[1:]:
    if i == prev:
        print(f'{i}')
    else:
        prev = i
"""
Find the duplicate number in the array using O(n) time complexity and O(1) space complexity.

Solution - 6
Ex-
a  = [5, 4, 1, 2, 3, 5]
Step-1: Check a[a[0]] -> a[5] and if its > 0, a[a[0]] = - a[a[0]].
Step-2: Else, Duplicate exists.
Step-3: Repeat for all the Elements of the list.

OutPut:
Print all the duplicate numbers i.e 5

Constraints:

1. Values in the list should be in the range of 0 to len(a) - 1
2. This solution doesn't work if array is ReadOnly.
3. This solution only works if all the elements in the list are positive.


"""
print('********Solution - 6*********')
my_list = [5, 4, 1, 2, 3, 5]
for i in range(len(my_list)):
    if my_list[abs(my_list[i])] < 0:
        print(f'{abs(my_list[i])}')
    else:
        my_list[abs(my_list[i])] = - my_list[abs(my_list[i])]

"""
Solution-7 : Traverse through list , and save sum of reminders*length of list so that we can later 
divide by len(list) to get the number of repetition. If repetitions > 1 , duplicate exists.     
"""
print('********Solution - 7********')
my_list = [5, 4, 1, 2, 3, 5]
for i in range(len(my_list)):
    my_list[my_list[i] % len(my_list)] += len(my_list)

for i in range(len(my_list)):
    freq = my_list[i] // len(my_list)
    if freq > 1:
        print(f'Duplicate Elements At Index: { i } exists:{ freq } times')

"""
Output::

*******Solution - 1*********
Duplicate Elements :
5
**********Solution - 2**********
5
********Solution - 3**********
5
*******Solution - 4********
5 is repeated 2 times
********Solution - 5**********
5
********Solution - 6*********
5
********Solution - 7********
Duplicate Elements At Index: 5 exists:2 times
"""
