from functools import wraps


# This is continuation from Functions_trick.py.  Due to powerful nature of functions, they can be used to decorate
# any functions. Lets take a look at a complex decorator
def strong(func):
    def wrapper():
        return '<strong>' + func() + '<strong/>'

    return wrapper


def bold(func):
    def wrapper():
        return '<bold>' + func() + '<bold/>'

    return wrapper


# Now, lets apply above decorators to the functions.

def yell():
    ''' Im an Yell Function'''
    return "Hello"


decorated_yell_1 = strong(yell)
print(decorated_yell_1())  # It prints, <strong>Hello<strong/>
# Lets apply another deocrator bold to the resultant function.
decorated_yell_2 = bold(decorated_yell_1)
print(decorated_yell_2())  # It prints <bold><strong>Hello<strong/><bold/>


# However, easier way to apply all decorators to the original function at once is using @ syntax as:

@bold
@strong
def yell():
    ''' Im an Yell Function'''
    return "Hello"


print(yell())  # This prints <bold><strong>Hello<strong/><bold/>

# Lets see the metadata of the function yell when decorators are applied to it.

print (yell.__name__, yell.__doc__)  # ('wrapper', None)


# Unfortunately, my metadata of the original functions get lost due to Decorators i.e they are not carried forward to
#  nested functions within the decorator/outer func.  The solution to this is to use, functiontools.wraps

def strong(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '<strong/>'

    return wrapper


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return '<bold>' + func(*args, **kwargs) + '<bold/>'

    return wrapper


@bold
@strong
def yell(input_):
    ''' Im an Yell Function'''
    return "Hello" + str(input_)


print(yell(" World!"))
print (yell.__name__, yell.__doc__)  # It now prints, ('yell', ' Im an Yell Function')
