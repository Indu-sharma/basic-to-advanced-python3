"""
Python2 and Python 3 has different property of print. 
Let's use this case to create different factories of Python versions & have different print implementation.   
"""


class Python2:
    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__} '


class Python3:
    def __init__(self, command):
        self._command = command

    @property
    def print_method(self):
        return f'{self._command} from concrete class : {self.__class__.__name__} '


class PythonFactory:
    def __init__(self):
        pass

    @staticmethod
    def my_factory(version, command):
        return {
            2: lambda x: Python2(x),
            3: lambda x: Python3(x)
        }.get(version)(command)


# Python 2
factory = PythonFactory()
python2 = factory.my_factory(2, 'print')
print(python2.print_method)

# Python 3
factory = PythonFactory()
python3 = factory.my_factory(3, 'print')
print(python3.print_method)
