class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


Obj =  MyNumbers().__iter__()
print( Obj.__next__() )
print( Obj.__next__() )
print( Obj.__next__() )
print( Obj.__next__() )
print( Obj.__next__() )
print( Obj.__next__() )

