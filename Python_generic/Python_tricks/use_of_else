"""
In Python, Else can be used along with For Loops and Try/Except as well.
In Case of Try/Except, Else block will be executed only if Try block is successful
and In case of Loops, Else block will be executed only of there is "no break" in the Loops.
Following two examples illustrate the Use of Else in both the scenarios:

"""

print(f'Accessing Main Docstring : {__doc__}')


def use_of_else_1(x, count=0):
    """
    Scenario - 1: Use of Else in Try/Except. Here Count will only be incremented if int(x) is successful
    """
    count = count + 1
    try:
        y = int(x)
    except ValueError as e:
        yield count

    else:
        count = count + 1
        yield count


print(f"{use_of_else_1.__name__} : {use_of_else_1.__doc__}")

for c in use_of_else_1('x'):
    print(f'Count = {c}')


def use_of_else_2():
    """
    Scenario - 2: Use of Else in For Loop. Print statement is executed only if the if within for Loop passes or Loop Breaks.
    """
    integer_list = [1, 2, 3, 'x']
    for i in integer_list:
        print(i, end=' ')
        if isinstance(i, str):
            break
    else:
        print(f"List: {integer_list} Contains Pure Integer Values")


print(f"{use_of_else_2.__name__} : {use_of_else_2.__doc__}")

use_of_else_2()
