"""
This is an example of how to define a class,
instantiate several objects, and use the object's method.
This file has been setup so that it can be imported as a module or run as a script.
"""

class Kangaroo:

    # Constructor method
    def __init__(self,name,age,gender):

        # Define instance attributes
        self.name = name
        self.age = age
        self.gender = gender

    # Method
    def greeting(self,your_name):

        print("G'day " + your_name + ", my name is " + self.name)

if __name__ == '__main__':
    # This code block executes if the file is run as a script

    # Instantiate a Kangaroo class object
    roo1 = Kangaroo(
        name = 'Bobbie',
        age = 5,
        gender = 'Female')

    # Instantiate another Kangaroo class object
    roo2 = Kangaroo(
        name = 'Lyle',
        age = 8,
        gender = 'Male')

    # Test the greeting method
    roo1.greeting('Crocodile Dundee')

    # Test the greeting method using another object's name attribute
    roo2.greeting(roo1.name)