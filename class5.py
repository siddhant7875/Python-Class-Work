"""
to understand the meaning of classes we have to understand
the built-in _init_() function

all classe have function called_init_(),which is always executed
when the class is being initiated. use the_init_() function to assign
valuesto object properties or other operations that are necessary to do
when the object is being created

"""
class Person:
  def __init__(self, name, age):
    self.name = name 
    self.age = age

p1 = person("John",36)

print(p1.name)
print(p1.age)