#!/usr/bin/python3 

"""
Today's Goal: 
1. Dictionary in Python
2. Solve a typical Dictionary problem
"""
# name, class, subject, score 

mydict = {'name': 'vivek', 'score':100} 
mydict1 = dict(name='vivek', score=100)
mydict['class'] = 1 # setting a K, V
print(mydict['score']) # Accessing value

mydict2 = dict([('name','vivek'), ('score',100)])

# print(list(mydict2.items())[0])

for k,v in mydict.items():
    print(k, v)
for k in mydict.values():
    print(k)
for v in mydict.values():
    print(v)

# Sorting 
my_l =  mydict.items()
my_sorted = sorted(my_l, key=lambda x: str(x[1]), reverse=True)
print(dict(my_sorted))




















