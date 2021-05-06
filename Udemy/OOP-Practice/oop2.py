class Circle():

    # Class Attributes
    pi = 3.14

    def __init__(self, radius = 1):

        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(30)

print(my_circle.get_circumference())
print(my_circle.area)