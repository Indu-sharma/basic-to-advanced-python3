"""
Given an array A of Integers find (i,j,k) such that A[i]^2+A[j]^2=A[k]^2
Ex -
A = [1,2,5,3,4,6]

Output : 3,4,5

Solutions:
1. Iterative Solution using Nested loops. Time Complexity : O(N^3).
2. Using Sorting As: 
    A.Sort the List.
    B. Scan and store the Square of each element.
    C. Scan new new array and for each elements in the array:
        1. Scan again from Left and Right and check if l + r == cur. If yes print.
        2. If l + r > cur , r-- ; else l++
    Time Complexity for this approach is : O(N^2) + NLogN (for Sorting) = O(N^2) 

"""
import math


def solution2(my_list: list) -> None:
    # Store the sorted of each elements squared . 
    my_list = sorted(map(lambda x: x ** 2, my_list))
    _len = len(my_list)
    res = []
    # Now Find Out Integers in the list which sum up to every elements of above Squared List. 
    for k in my_list:
        low = 0
        high = _len - 1
        while low < high:
            if my_list[low] + my_list[high] > k:
                high -= 1
            elif my_list[low] + my_list[high] < k:
                low += 1
            else:
                triplet = [my_list[low], my_list[high], k]
                triplet = tuple(map(int, map(math.sqrt, triplet)))
                res.append(triplet)
                low += 1
                high -= 1
    print(res)


my_list = [1, 2, 5, 3, 4, 6]
solution2(my_list)
