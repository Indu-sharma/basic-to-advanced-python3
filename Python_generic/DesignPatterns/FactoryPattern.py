from abc import ABC, abstractmethod

class Animal(ABC):
    ''' The methods marked as abstractmethod should be implemented in the child class
    Otherwise, we get the notImplementedError derived from RunTimeError exception'''
    
    @abstractmethod
    def do_say(self):
        pass

class Dog(object):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(object):
    def do_say(self):
        print("Mew mew!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        if hasattr(eval(object_type),"do_say"):
            return eval(object_type)().do_say()
        else:
            print("Factory class is trying to access method that doesnt exist in {}".format(eval(object_type)))


ForestFactory().make_sound("Cat")

