import inspect

mylist = [1, 6, 4, 2, 9, 3]

"""
Compare the Adjacent elements and swap them.

"""


def bubble(my_list):
    length = len(my_list)
    k = 0
    while k <= length:
        swapped = False
        for i in range(1, length):
            if my_list[i] < my_list[i - 1]:
                continue
            else:
                swapped = True
                my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
        if not swapped:
            break
        k += 1
    print(inspect.stack()[0][3], end=': ')
    print(my_list)


bubble(mylist)

"""
Select the Minimum value and compare with the rest of elements and put into appropriate position.
 
"""


def selection(my_list):
    length = len(my_list)
    for i in range(length):
        minimum = i
        for j in range(i, length):
            if my_list[i] < my_list[j]:
                minimum = j
        my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
    print(inspect.stack()[0][3], end=': ')
    print(my_list)


selection(mylist)


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    first_half = merge_sort(my_list[:mid])
    second_half = merge_sort(my_list[mid:])
    return merge(first_half, second_half)


def merge(mylist1, mylist2):
    i = 0
    j = 0
    merged_list = []
    n1 = len(mylist1)
    n2 = len(mylist2)

    while i < n1 and j < n2:
        if mylist1[i] > mylist2[j]:
            merged_list.append(mylist1[i])
            i += 1
        else:
            merged_list.append(mylist2[j])
            j += 1

    merged_list = merged_list + mylist1[i:] + mylist2[j:]
    return merged_list


final_list = merge_sort(mylist)
print(f'Merge: {final_list}')
