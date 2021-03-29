class property_decorator(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)

    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @fullname.setter
    def fullname(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]


my_object = property_decorator("indu", "sharma")
print my_object.fullname


my_object.fullname = "raju Sharma"
print my_object.fullname

