#*************************************Example Program Classes and Inheritance**************************************
import math
class Point:
    #takes an x and y value
    def __init__(self, ix, iy):
        self.x = ix
        self.y = iy
        
class Line:
    def __init__(self, p1x, p1y, p2x, p2y):
        # creates points by calling the point class inside the line class using composition instead of inheritance
        self.p1 = Point(p1x, p1y)
        self.p2 = Point(p2x, p2y)
    def getLength(self):
        #pythag for distance d = sqrt((x2-x1)^2 + (y2-y1)^2)
        # find the differences of x and y
        difx = self.p2.x - self.p1.x
        dify = self.p2.y - self.p1.y
        # calc distance
        return math.sqrt(difx * difx + dify * dify)
    
class Circle(Point):
    # circle class uses inheritance from the point class for the x and y values
    def __init__(self, ix, iy, d):
        self.diameter = d
        super().__init__(ix, iy)
    def getCircumference(self):
        # c = 2*pi*r
        return 2 * math.pi * (self.diameter / 2)
    
l = Line(1, 4, 5, 1)
c = Circle(0, 0, 10)
print(l.getLength())
print(c.getCircumference())
    