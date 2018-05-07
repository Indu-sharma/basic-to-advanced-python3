"""Functions in Python are first class citizen i.e Functions are objects that can be returned, passed as arguments to
another functions, can be stored as objects in other structures, can nests other functions too & nested functions
remembers the states of parent functions. These are the features which make python function a really powerful,
and helps the functional programming in python. Function nestings, functions returning function example:"""


def myouter(text, volume):
    def myupper():
        return text.upper() + '!'

    def mylower():
        return text.lower() + '!'

    if volume > 0.5:
        return mylower
    else:
        return myupper


print myouter("Hello, World", 0.7)()  # o/p : hello, world!
print myouter("Hello, World", 0.3)()  # o/p : HELLO, WORLD!


# Note: Functions names are created only once in first call, Example:


def originalfunc():
    return 43


copyfunc = originalfunc

del originalfunc

print(copyfunc())  # Its obvious it will just print 43
print(copyfunc.__name__)  # This wouldnt print copyfunc, but originalfunc


# What about the Class objects act like a callable function ? Lets see, its possible with __call__ method override

class MakeCallable:
    def __init__(self):
        self.value = 10

    def __call__(self, *args, **kwargs):
        print self.value + sum(args) + sum(kwargs.values())


myobj = MakeCallable()

myobj(10)
# This results 20 & True i.e its callable.Notice here we are calling the Instance object just like function call.
# Its possible due to __call__

print(callable(myobj))

# Lambda functions are the expressions that cant have multiple statements nor the return statements.
# However, Lambda Functions also have similar features as that of normal functions defined using def keyword

# 1 Lambda  functions can be assigned and be evaluated lazily like normal functions

adder = lambda x, y: x + y
res = adder(12, 20)
print(res)

# 2 Lambda functions can be evaluated at the time of defination, example:

res = (lambda x, y: x + y)(12, 20)
print(res)

# 3 Lambda  functions are really useful in sorting key for non-default sort-key as:

mylist = [(1, 2), (10, 20), (0, 1), (10, 100), (3, 80)]
res = sorted(mylist, key=lambda x: x[1])
print(res)


# 4  Lambda functions can be used as Lexical closures i.e nested functions with global scoping of parent functions


def myadder(value):
    return lambda x: x + value


res = myadder(10)(100)

print(res)
