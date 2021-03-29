from abc import ABCMeta, abstractmethod

"""
Python2 and Python 3 has different property of print. 
Let's use this case to create different factories of Python versions & have different print implementation.   
"""

class Factory(metaclass=ABCMeta):

    @abstractmethod
    def my_factory(self, version, command):
        pass


class PythonFactory(Factory):
    def __init__(self):
       pass

    def my_factory(self, version, command):
        return {
            2: lambda x: Python2(x),
            3: lambda x: Python3(x)

        }.get(version)(command)


class Python(metaclass=ABCMeta):

    @abstractmethod
    def print_method(self):
        pass


class Python2(Python):

    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__} '


class Python3(Python):
    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__} '


# Python 2
factory = PythonFactory()
python2 = factory.my_factory(2, 'print')
print(python2.print_method)

# Python 3
factory = PythonFactory()
python2 = factory.my_factory(3, 'print')
print(python2.print_method)
