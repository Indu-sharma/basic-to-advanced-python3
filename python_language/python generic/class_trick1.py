# Is and == operators works differently in python in the sense former is for the Object pointer comparision and later
#  is for the values comparision. lets c by example.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# First prints True, but second prints False. Why lets c the object pointer to see
print(id(a), id(b))

# This prints different memory addresses i.e (4554366056, 4554366776)
# Hence, is operator always compares the id of objects not the values.
# lets take another example where the ID of objects are same.

a = [1, 2, 3]
b = a

print(a is b)
print(id(a), id(b))

# The print statement prints True because the IDs of a & b is same i.e (4449578736, 4449578736)


# __str__ & __repr__ in python class. Former is for the user & later is for the programmer by convention.
# Lets c with the example.

import datetime

today = datetime.date.today()
print(today)  # It prints 2018-05-05
print(repr(today))  # It prints datetime.date(2018, 5, 5)


# In Python 2.x, __str__ returns the bytes & __unicode__ returns the characters. Hence its better to implement both
# the methods in class as:

class Test:
    def __init__(self):
        self.mylist = []

    def adder(self, x):
        if isinstance(x, list):
            self.mylist.extend(x)
        else:
            self.mylist.append(x)

    def __unicode__(self):
        return u'current list {self.mylist}'.format(self=self)

    def __str__(self):
        return unicode(self).encode('utf-8')


myobj = Test()
myobj.adder([10, 100, 200])

print(myobj)

