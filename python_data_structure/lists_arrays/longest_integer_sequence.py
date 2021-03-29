"""
There is an Integer Array.
Ex - My_list = [0, 9, 9, 9, 9, 8, 7, 6, 1, 5, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 5,5,5,5,5,5]
Expected : Give the length of maximum Sequence of consecutive occurrence of an Integer
OutPut: 5, 1
Step-1: Traverse from Start.
Step-2: Check current integer with previous. Keep track of   : count & Max_len
Step-3: If Current Integer & prev are same , Increase the Count.
Step-4: Else - check if the current count is > Max_len  & re-set max_len to current count.
and reset the count.
Step-5: At the end print the Max_len.
Step-6: Handle the End case.
"""


def longest_seq(my_list):
    my_len = len(my_list)
    if my_len < 1:
        return
    count = 1
    max_len = 0
    int_value = my_list[0]
    for i in range(1, my_len):
        if my_list[i] == my_list[i - 1]:
            count = count + 1
        else:
            if count > max_len:
                max_len = count
                int_value = my_list[i - 1]
            count = 1
    if count > max_len:
        max_len = count
        int_value = my_list[-1]
    return max_len, int_value


# Driver Code

if __name__ == '__main__':
    my_list = [0, 9, 9, 9, 9, 8, 7, 6, 1, 5, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 5,5,5,5,5,5]
    max_count, value = longest_seq(my_list)
    print(
        f'Longest consecutive Integer Sequence is: {",".join([str(value)] * max_count)} and Length of sequence is :{max_count}')
