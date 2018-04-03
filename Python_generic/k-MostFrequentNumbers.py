def k_most_frequent(k, input_arr):
    """ Given an Array find the Most K-frequent Numbers"""
    results = []
    mapdict = {}
    my_bucket = [0] * len(input_arr)
    for i in input_arr:
        if i in mapdict:
            mapdict[i] += 1
        else:
            mapdict[i] = 1
    for key in mapdict:
        value = mapdict[key]
        if my_bucket[value] == 0:
            my_bucket[value] = [key]
        else:
            my_bucket[value].append(key)
    i = len(my_bucket) - 1
    while i >= 0:
        if my_bucket[i] != 0:
            if len(my_bucket[i]) == k:
                results.extend(my_bucket[i])
                break
            elif len(my_bucket[i]) < k:
                results.extend(my_bucket[i])
                k -= len(my_bucket[i])
                i -= 1
            else:
                results.extend(my_bucket[i][0:k])
                break
        else:
            i -= 1
    return results


# Testing/Driver code

input_arr = [1, 3, 4, 5, 6, 7, 8, 4, 4, 8, 10, 20, 17, 15, 1, 3, 5]
k = 5

print(k_most_frequent(k, input_arr))

# O/p : [4, 1, 3, 5, 8]
