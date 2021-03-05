# Method 1 :: Using Decorators


def mysingleTon(MyClass):
    instances = {}

    def mysingleTon(*args,**kwargs):
        if MyClass not in instances:
            instances[MyClass] = MyClass(*args,**kwargs)
        return instances[MyClass]

    return mysingleTon


@mysingleTon
class SingleTon(object):
    def __init__(self):
        self.mylist = []

    def implement_list(self,num):
        self.mylist.append(num)

    def get_list(self):
        return self.mylist

myobj=SingleTon()
myobj.implement_list(10)
myobj.implement_list(20)
print(myobj.get_list())

myobj1=SingleTon()
myobj1.implement_list(30)
myobj1.implement_list(40)
print(myobj1.get_list())

##ethod 2 Using Class Methods


class SingleTon1(object):
    """SingleTon With Class Method"""
    _instances = None
    

    def __init__(self):
        self.mylist = []
        print("Hey There {}".format(SingleTon1._instances))

    def implement_list(self,num):
        self.mylist.append(num)

    @property
    def get_list(self):
        return self.mylist

    @get_list.setter
    def get_list(self, mylist):
        self.mylist = mylist

    @classmethod
    def getInstance(cls):
        if not cls._instances:
            cls._instances = SingleTon1()
        return cls._instances

myobj = SingleTon1.getInstance()
myobj.get_list = [1,2,3]
myobj.implement_list(10)
myobj.implement_list(20)
print(myobj.get_list)
myobj1 = SingleTon1.getInstance()
myobj1.implement_list(30)
myobj1.implement_list(40)
