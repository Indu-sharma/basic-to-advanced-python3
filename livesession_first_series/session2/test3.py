"""

Today's scope :
    part1 :: Python Packages (Folder having __init__.py file ; it can be empty)
part2 - Visit some important == string methods ::: Concat, strip, replace, split and format


"""
import session1.test1 as st1
n = 2
my_fmt = '{session} is my session from class {_class}'
my_input = st1.__name__  # Gets the name space.
_class = 2
my_float = 2.000001

if __name__ == '__main__':
    """
    --->OutPut of this program will be --> 
    Current Session is:::::session1.test1
    session1.test1 is my session from class 2
    session1.test1 is my session.
    Truncated float of 2.000001 is: 2.00 and binary 2 is: 10
    """

    print('Current Session is'+':'*5+my_input)   # String concat using + and *
    print(my_fmt.format(_class=_class, session=my_input))  # Using Format
    print(f'{my_input} is my session.\nTruncated float of {my_float} is: '
          f'{my_float:.2f} and binary {n} is: {n:b}') # Using F-string.



