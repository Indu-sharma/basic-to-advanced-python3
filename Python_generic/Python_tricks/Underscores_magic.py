"""Private just by convention, use single _ at the start i,e intended to access from within the class or module
However, if the module is imported as from Underscores_magic import *, the variables with _ as prefix are not imported
unless its added as a part of __all__ list."""


def _myfunc():
    return 52


class MyClass:
    _private = None

    def __init__(self):
        pass


"""Single Underscores at the end of variables is by PEP-8 is used as resolution of conflicts while using inbuilt 
variables """


def myfunc(class_):
    return class_


def myfunc1(def_):
    return def_


"""Doube _ i.e __ at the start prevents the direct access in classes variables or methods 
from outside. This is done to resolve the conflicts in the inhereted class by incorporating _<ClassName> prefix 
to such variables or methods"""


class Test:
    def __init__(self):
        self.__mangled = 100

    def call_mangled(self):
        return self.__mangled


print(Test().call_mangled())  # It prints 100
print(Test()._Test__mangled)  # It prints 100


# print(Test().__mangled)  # It raises AttributeError

class TestEx(Test, object):
    def __init__(self):
        """Super can only be used only if inhereted from New stlye class, otherwise Object should be provided in the
        child class. Make sure to put object at the end to get this, first understand MRO """
        super(TestEx, self).__init__()

    def call_mangled(self):
        return self._Test__mangled  # just returning self.__mangled throws exception.


print(TestEx().call_mangled())


# Another way would be like this:


class TestGlobal:
    _TestGlobal__mangled = 101

    @property
    def call_mangled(self):
        return self.__mangled  # This will be converted to _Test__mangled & global value would be returned.


print(TestGlobal().call_mangled)

# Just Underscore _ is usually helpful to get the result of last execution output in terminal or incase u just don't
# care about using it.

for _ in range(3):
    print("Hello, World!")

a, _, c, _ = 1,2,3,4

print(a, c, _) # It will print a & c, _ overwrites from right to Left incase of multiple ones.
