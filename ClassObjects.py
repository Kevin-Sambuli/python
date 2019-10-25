""" CLASSES AND OBJECTS"""
"""Class """
# is a blue print of creating an object
# we create a class to define the nature of a future object
# a class has properties and actions which are methods
"""Object"""
# is an instantiation of a class

"""syntax"""
# class Classname:(class name must start with a capital letter)
#     body of the class


class Person:
    # name = "Sambuli"
    name = None
    age = None
    gender = None

p1 = Person()
p1.name = "Kevin"
print(p1.name)

p2 = Person()
p2.name = "Sambuli"
print(p2.name)


class Car:
    type = "Toyota"
    model = None
    engine = None
    color = None

car1 = Car()
car1.model = "prado"
car1.color = "black"
car1.engine = "V8"


"""Methods"""
