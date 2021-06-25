#!/usr/bin/python3
"""
Today's scope :

1. Map/Filter/Reduce in Python   
"""
from functools import reduce

my_list = [10,20,29, 30,40, "Hi","hello"] 
# I want to produce : 10203040 
my_list1 = []
for i in my_list:
    i = str(i)
    my_list1.append(i)
res = ''.join(my_list1)

# print(res)

# res = sum(map(lambda x: x**3, my_list))
# print(res)
# my_list = [[10,20],[30,40,50],[1,2,3,4]]
# # Output: [2,3,4]
# res = list(map(len, my_list))
# print(res)

# print(''.join(map(lambda x: x**3, my_list)  ))

# res =filter(lambda x: x%2!=0, my_list)
# print(list(res))

my_list = [10,20,29, 30,40] 
res =sum(filter(lambda x: isinstance(x, int) and x%2!=0, my_list))
print(res)


my_list = [10,20,29, 30,40] 
# Multiply all the elements of the list. 

mul = reduce(lambda x,y: x*y,my_list)
print(mul)

# Fact of 5 
def fact(n):
    fact = reduce(lambda x,y:x*y, range(1,n+1))
    print(fact)
fact(6)


