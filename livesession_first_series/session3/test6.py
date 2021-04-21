"""
Flatten the list with nested list reversed:

I/P - [10,[1,2,3],[5,6,7],[7,8,9]]
O/p - [10,3,2,1,7,6,5,9,8,7]

Constraints:
- Input has at Max Single Nesting.
- Space Complexity should be O(1)
- Time Complexity should be O(N)

"""

# Basic concepts
my_list = [1, 4, 5, 7, 'hello']
# List slicing - my_list[start:end:step] ; start is inclusive index & end is exclusive.
var = my_list[1:3]  # it will print [4,5]
my_list1 = my_list     # IDs of my_list & my_list1 will be same.
my_list2 = my_list[:]  # IDs of my_list & my_list1 will be Different
print(id(my_list), id(my_list2))
length = len(my_list)  # Gives the Length of List
print(my_list[-length]) # Negative Index ; it will result 1.
x = 'ANA'
print(x[::-1] == x)  # Check if x is palindrome or not.

# Solution1 to Above problem; Space Complexity O(1)

my_list = [10, [1, 2, 3], [5, 6, 7], [7, 8, 9]]
my_len = len(my_list)
i = 0
while True:
    try:
        n = my_list[i]
    except IndexError as e:
        break
    if isinstance(n, list):
        my_list[i:i + 1] = n[::-1]
        i = i + len(n)
    else:
        i = i + 1
print(f'solution1 - {my_list}')

# Solution 2 to Above problem; Space Complexity O(N).
out_list = []
for e in my_list:
    if isinstance(e, list):
        out_list.extend(e)
    else:
        out_list.append(e)
print(f'solution2 {out_list}')
