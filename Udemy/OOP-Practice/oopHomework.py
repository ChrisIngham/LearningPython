import math

# LINE QUESTION
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    # Distance  = sqrt[ (x2-x1)^2 + (y2-y1)^2 ]
    def distance(self):
        return math.sqrt( ((self.coor2[0] - self.coor1[0]) ** 2) + ((self.coor2[1] - self.coor1[1]) ** 2) )

    # Slope = ( y2 - y1 ) / ( x2 - x1 )
    def slope(self):
        return ( (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print("Distance of Line: ", li.distance())
print("Slope of Line: ", li.slope())


# CYLINDER QUESTION
class Cylinder:

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    # Volume = pi * radius^2 * height
    def volume(self):
        return (self.pi * (self.radius ** 2) * self.height)

    # Surface Area = (2 * pi * radius * height) + (2 * pi * radius^2)
    def surface_area(self):
        return ( (2 * self.pi * self.radius * self.height) + (2 * self.pi * ((self.radius) ** 2)))

c = Cylinder(2,3)
print("The Volume is: ", c.volume())
print("The Surface Area is: ", c.surface_area())
