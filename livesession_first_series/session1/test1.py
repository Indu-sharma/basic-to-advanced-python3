"""
Today's scope:
part1:: Namespace, basic scalar python data types
part2:: Understanding methods with Dir & Help  keywords.
part3:: Python Modules
"""

my_string = 'Hello World!'
my_int = 1
my_float = 4.5

if __name__ == '__main__':
    print("Im calling this from the original:", my_string, my_float, my_int)
    print(dir(my_string))  # This gives you all the string methods available in Python.
    print(help(my_string.isdigit))  # This gives you the Syntax for isdigit method.
    print(my_string.isalpha())
