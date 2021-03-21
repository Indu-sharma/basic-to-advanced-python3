"""
Given an Array of positive Integers, find the pair of numbers such that they sum up to k.
0 < k < N
Ex:
My_list = [7,6,9,10,12,1,4,3]
k = 15

Output : return the list of Pairs i.e [(6,9),(12,3)]
Solution:

Following are the possible solutions
1. Use Iterative method - nested loops and check all possible pairs to sum up to k.
Time Complexity - O(n^2) & Space Complexity - O(1)
2. Use Sorting and scan from left and right to sum up to k; if sum > k , increment left else increment right.
Time Complexity - O(N*LogN) & Space Complexity - O(1).
3. Use Hashing method to store the Integers and check if k - current integer exist in the hash table.
Here third is the most efficient method in terms of Time Complexity->O(N). However, space complexity is O(N).

Lets implement them 1 by 1.
"""


def solution1(my_list, k):
    res = []
    _len = len(my_list)
    for i in range(_len):
        for j in range(i + 1, _len):
            if my_list[i] + my_list[j] == k:
                res.append((my_list[i], my_list[j]))
    print(f'Solution -1 result : {res}')


def solution2(my_list, k):
    res = []
    my_list.sort()
    _len = len(my_list)
    low = 0
    high = _len - 1
    while low < high:
        if my_list[low] + my_list[high] > k:
            high -= 1
        elif my_list[low] + my_list[high] < k:
            low += 1
        else:
            res.append((my_list[low], my_list[high]))
            low += 1
            high -= 1

    print(f'Solution -2 result : {res}')


def solution3(my_list, k):
    my_dict = {}
    res = []
    for i in my_list:
        if i not in my_dict:
            my_dict[i] = 1

        if abs(k - i) in my_dict:
            res.append((i, abs(k - i)))

    print(f'Solution -3 result : {res}')


if __name__ == '__main__':
    """
    Output :
    Solution -1 result : [(6, 9), (12, 3)]
    Solution -2 result : [(3, 12), (6, 9)]
    Solution -3 result : [(9, 6), (12, 3)]
    """
    my_list = [7, 6, 9, 10, 12, 1, 4, 3]
    k = 13
    solution1(my_list, k)
    solution2(my_list, k)
    solution3(my_list, k)
