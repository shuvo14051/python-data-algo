"""
When we call a method of this object as myobject.method(arg1, arg2),
this is automatically converted by Python into
MyClass.method(myobject, arg1, arg2)  this is all the special self is about
"""

class SelfParameter:
    # if we omit self the following error occurs
    # hello() takes 0 positional arguments but 1 was given
    def hello(self):
        print("Hello World")


s = SelfParameter()
# this is the way python call the method
# the instance of a call is passed as a parameter
# that's why we need to use self


# we use this short hand way to call a method
# where we need to manually pass the instance as a parameter
# it is passed automatically

s.hello()

# SelfParameter.hello(s)

# the above line is equivalent to "SelfParameter.hello(s)"