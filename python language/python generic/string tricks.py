# The simplest String formatting way is :

name = "Indu"
error = 5678888

myformat = "Hey, {} the error is generated and code is {}"
print(myformat.format(name, hex(error)))

# however, here you need to take care of positional parameters! So we can have similar to below:

myformat = "Hey, {Name} the error is generated and code is {Err}"

print(myformat.format(Err=hex(error), Name=name))

# Lets consider the following example, where the format parameters are user inputs

SECRET = 'This-is-a-secret'


class Error:
    def __init__(self):
        pass


err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print user_input.format(error=err)

# This is really a security concern as User is able to use the format vulnarability.
# So this enforces us to explore the String format Template

from string import Template

myformat = "Hey, $Name the error is generated and code is $Err"
t = Template(myformat).substitute(Name=name, Err=hex(error))
print(t)

# Lets take a look at how this template formatting helps

user_input = '${error.__init__.__globals__[SECRET]}'

try:
    t1 = Template(user_input).substitute(error=err)
except ValueError as e:
    print("ValueError :{}".format(e))

# What if only the error is wrapped around with $

user_input = '${error}.__init__.__globals__[SECRET]'

t2 = Template(user_input).substitute(error=err)

print(t2)
# This time the object instances are not executed the way we wished.
# It just prints '<__main__.Error instance at 0x10a4ff3f8>.__init__.__globals__[SECRET]'
