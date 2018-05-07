# By default copy of the objects doesnt actually make the independent copy, but just referenced. Hence, changes in
# the original objects impacts the copied object and vice-versa. However, shallow copy make the independent copy of
# the the objects but at depth-1 i.e  child objects are still referenced.
# Hence there is a need for deepcopy, where the objects are actually copied along with its child.
# Shallow copy can be created by using the default factory methods like list(), dict(), set() etc or using copy.copy()
# Deep copy can be created by using the copy.deepcopy() method of the copy module.

import copy


def simulate_copy_add(mylist, mylist1):
    print ("Objects are same for both lists before add/modify?")
    print(mylist is mylist1)

    print ("Copy and original Lists elements are same  after addition of elements to lists?")
    mylist1.append(100)
    print(mylist == mylist1)


def simulate_copy_modify_del(mylist, mylist1):
    print ("Objects are same for both lists before del/modify?")
    print(mylist is mylist1)
    mylist[0][0] = mylist1[0][0] * 10
    del mylist[0][1]
    print ("Copy and original Lists elements are same  after deletion and modification of child of lists?")
    print  mylist == mylist1


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1 NormalCopy
mylist1 = mylist
simulate_copy_add(mylist, mylist1) # Prints True, True
simulate_copy_modify_del(mylist, mylist1)  # Prints True, True

# 2 ShallowCopy
mylist1 = list(mylist)
simulate_copy_add(mylist, mylist1) # Prints False, False
simulate_copy_modify_del(mylist, mylist1) # Prints False, True

# 3 DeepCopy

mylist1 = copy.deepcopy(mylist)

simulate_copy_add(mylist, mylist1) # Prints False, False
simulate_copy_modify_del(mylist, mylist1) # Prints False, False


'''Make sure to call above functions one by one and see the results.
Summary of Object copy with example list:
1> In Normal copy, the list object and copied list objects are same and so are the lists elements regardless of addition, 
deletion and modification of list elements.

2> In Shallow copy, the list object and copied list objects are different.
Incase of list elements additions, oroginal list elements and copy are not same.   
However, list elements are same on both the lists even after deletion or modification of old list elements.

3> In Deep Copy, the list object and copied list objects are different and so are the list elements regardless of addition, 
deletion and modification of list elements

'''