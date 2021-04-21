"""
Scope:
Part-1: How Integers and Strings are stored in Memory in Python 3.7+ ?size,type/isinstance,id,is,refcounts,intern
Part-2: List Basics: Properties , Methods & Slicing  
Part-3: Solve a typical list problem.  
"""
import sys

my_string = 'Hello World'
my_int = 1099
print(type(my_int))  # <class 'int'>
print(type(my_string))  # <class 'str'>
print(isinstance(my_int, int))  # True
print(sys.getsizeof(my_int))  # 28
print(sys.getsizeof(''))  # 49
my_int1 = 900
my_int2 = 900
print(id(my_int1), id(my_int2))  # Memory Locations are same for Integers till 1000
print(sys.getrefcount(my_int))
print(my_int1 is my_int2)  # compares the Memory Location i.e same objects.

# For String
my_string1 = 'h' * 4096
my_string2 = 'h' * 4096
print(id(my_string1), id(my_string2))
print(f'without Forced Interning, are two strings of length <= 4096 interned by default? \
      {my_string1 is my_string2}')

my_string1 = 'h' * 4097
my_string2 = 'h' * 4097
print(id(my_string1), id(my_string2))
print(f'without Interning, are two strings of length > 4096 interned by default? \
      {my_string1 is my_string2}')

my_string1 = sys.intern('h' * 4097)
my_string2 = sys.intern('h' * 4097)
print(id(my_string1), id(my_string2))
print(f'With Forced Interning, are two strings of length > 4096 interned? \
      {my_string1 is my_string2}')
