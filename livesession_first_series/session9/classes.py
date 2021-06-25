#!/usr/bin/python3

from multipledispatch import dispatch
from collections.abc import Iterable

# Class / Inheritence / Super  

class Test1:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
    
    def display(self):
        return self.name+str(self.rollNumber)


class Test2(Test1):
    def __init__(self, name, rollNumber, score):
        super().__init__(name, rollNumber)
        self.score = score
    
    def get_score(self):
        return f'{self.name} <=> {self.score}'

c = Test2("Indu", 100, 80.0)
res = c.display()
print(res)
res1 = c.get_score()
print(res1)


# Inheritence, Multi-level inheritence , Multiple Inheritence 

class A:
    pass
class B:
    def display(self):
        print("B")
class C(A):
    def display(self):  #Method Overriding
        print("C")
class D(B):
    pass
class E(D, A, B):
    pass 

obj = E()
obj.display() 
print(E.__mro__) # This gives methods Resolution Order incase of Inheritence 


# Class Methods, staticmethod & Property Decorators

class Test:
    mail = '@gmail.com'
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.employer()

    @property
    def email(self):
        return f'{self.fname}.{self.lname}{self.mail}'

    @classmethod
    def hotmail(cls):
        cls.mail = '@yahoo.com'
        return cls

    @staticmethod
    def employer():
        print('Wipro')

    def __str__(self):
        return f'{self.fname},{self.lname}'

    def ___add__(self, other):   # Operator Overloading 
        fname= self.fname+other.fname
        lname = self.lname+other.lname
        return fname, lname

c1 = Test('vinod','boruah')
c2 = Test('indu','sharma')
print(str(c1)+str(c2))



# Composition :: Get the distance between two Points (x1,y1) & (x2,y2)

import math
class Point:
    def __init__(self, a, b):
        self._points = (a,b) 

class Distance:
    def __init__(self,P1, P2):
        self.P1 = P1._points
        self.P2 = P2._points
    def calc_distance(self):
        return math.sqrt((self.P2[0] - self.P1[0])**2 + (self.P2[1] - self.P1[1])**2)

p1 = Point(1,0)
p2 = Point(0,1)
d = Distance(p1,p2).calc_distance() 
print(d)



# Function/method Overloading :: No direct support but we can achieve with multipledispatch module. 

@dispatch(int,float)
def multiply(a,b):
    print(f'Calling method with 2 arguments:{type(a)},{type(b)}')
    result = a*b
    print(result)

@dispatch(Iterable,int)  #Iterable :: List, Set, tuple etc.
def multiply(mylist,a):
    print(f'Calling method with 2 arguments:{type(mylist)},{type(a)}')
    result = [i*a for i in mylist]
    print(result);

@dispatch(int,float,float)
def multiply(a,b,c):
    print(f'Calling method with 3 arguments:{type(a)},{type(b)},{type(c)}')
    result = a * b * c
    print(result);

multiply(10,10.5) # Calls first function 
multiply([1,3,5],2) # Calls Second function 
multiply((1,3,5),2) # Calls Second function
multiply({1,3,5},2) # Calls Second function
multiply(10,10.5,20.5) # Calls third function 
