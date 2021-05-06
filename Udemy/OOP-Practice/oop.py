class Dog():

    # Class Object Attributes, Same for all classes
    species = 'Mammal'

    def __init__(self, breed, name):
        # Attributes
        self.breed = breed
        self.name = name

    # Operators / Actions --> Methods
    def bark(self, number):
        for i in range(number):
            print("WOOF! My name is {}".format(self.name))



my_dog = Dog('Bernese', 'Luna')

my_dog.bark(9)