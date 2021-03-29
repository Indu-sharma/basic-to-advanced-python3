"""
@author : Indu Sharma
@version: 1.0.0
@summary: Find the number of all possible sub-sets from the given set that sums to given k.

Solution: Traverse the array and check if given element can be included or excluded to make given total.
If its included, then the new total would be reduced to (total - current element).

Base Condition:
1. If total is zero , then there is at least 1 set that sums to given k or total.
2. if total < zero, then there are no sets which sums to given k or total.
3. If before above 2 condition, all elements of the sets are visited,
then there are no sets which sum to given k or total.

Recursive Condition(s):
1. If current element > current total, then  include current element i.e
subSetSum(inputSet, k, i + 1)
2. Otherwise if you have two possibilities :
i. You may get the sum total with including the current element
ii. You may get the sum total without including the current element.
Summing i & ii will give the number of subsets that sum to k which would include/exclude current element.

"""


def subSetSum(inputSet, k, i=0) -> int:
    """
    @type i: int
    @type k: int
    @type inputSet: Set
    """

    if k == 0:
        return 1
    elif i > len(inputSet) - 1:
        return 0
    elif k < 0:
        return 0
    elif inputSet[i] > k:
        return subSetSum(inputSet, k, i + 1)
    else:
        return subSetSum(inputSet, k, i + 1) + subSetSum(inputSet, k - inputSet[i], i + 1)


if __name__ == '__main__':
    inputSet = {2, 4, 8, 6, 10}
    k = 10
    print(subSetSum(list(inputSet), k))
    """
    Output : 3 
    Subsets : {2,4,6} {4,6} {10} 
    """
