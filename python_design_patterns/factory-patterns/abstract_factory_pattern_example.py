from abc import ABCMeta, abstractmethod

"""
Python2 and Python 3 has different property of print. 
Let's use this case to create different factories of Python versions & have different print implementation.   
"""

class PythonFactory(metaclass=ABCMeta):

    @abstractmethod
    def my_factory(self, version, command):
        pass


class Python2Factory(PythonFactory):
    def __init__(self):
        pass

    def my_factory(self,version,command):
        return {
            20: lambda x: Python20(x),
            27: lambda x: Python27(x)

        }.get(version)(command)


class Python3Factory(PythonFactory):
    def __init__(self):
        pass

    def my_factory(self, version, command):
        return {
            30: lambda x: Python30(x),
            37: lambda x: Python37(x)

        }.get(version)(command)


class Python2(metaclass=ABCMeta):

    @abstractmethod
    def print_method(self):
        pass


class Python20(Python2):

    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__} '


class Python27(Python2):

    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__}'


class Python3(metaclass=ABCMeta):

    @abstractmethod
    def print_method(self):
        pass


class Python30(Python3):
    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__}'


class Python37(Python3):
    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__}'


# Python 2 i.e Python 2.0 & 2.7

py2_factory = Python2Factory()
concrete1 = py2_factory.my_factory(20,'print')
print(concrete1.print_method)
concrete2 = py2_factory.my_factory(27,'print')
print(concrete2.print_method)

# Python 3 i.e Python 3.0 & 3.7

py3_factory = Python3Factory()
concrete1 = py3_factory.my_factory(30,'print')
print(concrete1.print_method)
concrete2 = py3_factory.my_factory(37,'print')
print(concrete2.print_method)
