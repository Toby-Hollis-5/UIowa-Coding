import math

class Circle:
   
    def __init__ (self, centerX = 0.0, centerY = 0.0, radius = 0.0):
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        
    def getCenter(self):
        return (self.centerX, self.centerY)

    def setCenter(self, x, y):
        self.centerX = x
        self.centerY = y
    
    def getRadius(self):
        return self.radius
    
    def move(self, xChange, yChange):
        self.centerX = self.centerX + xChange
        self.centerY = self.centerY + yChange

    def isBigger(self, otherCircle):
        return self.radius > otherCircle.getRadius()

    def __lt__(self, otherCircle):
        return otherCircle.isBigger(self)

    def area(self):
        return math.pi * self.radius * self.radius
    
    def circumference(self):
        return math.pi * 2 * self.radius
    
    def distanceBetweenCenters(self, otherCircle):
        return math.sqrt((otherCircle.centerY-self.centerY)**2 + (otherCircle.centerX - self.centerX)**2)

    def intersects(self, otherCircle):
        distanceBetweenCenters = self.distanceBetweenCenters(otherCircle)
        return(distanceBetweenCenters <= (self.radius + otherCircle.getRadius()))
    
    def __repr__(self):
        return '< circle with radius {} centered at ({},{}) >'.format(self.radius,  self.centerX, self.centerY)
    
def testCircle():
    circle1 = Circle(0.0, 0.0, 1.0)
    print("Circle 1:", circle1)
    print("Circle1 has circumference:", circle1.circumference())
    print("Circle1 has area:", circle1.area()) 
    circle2 = Circle(0.0, 0.0, 2.0)
    print("Circle 2:", circle2)
    print("Result of circle1.intersects(circle2) is: {}".format(circle1.intersects(circle2)))
    circle2.move(3.0, 0.0)
    print("Moved circle 1 to (3,0)")
    print("Result of circle1.intersects(circle2) is: {}".format(circle1.intersects(circle2)))
    circle2.move(.001, 0.0)
    print("Moved circle 1 to (3.001,0)")
    print("Result of circle1.intersects(circle2) is: {}".format(circle1.intersects(circle2)))
    circle3 = Circle(1.0, 1.0, 1.0)
    print("Circle 3:", circle3)
    print("Result of circle1.intersects(circle3) is: {}".format(circle1.intersects(circle3)))
    circle3.move(1.0,1.0)
    print("Moved circle 3 by (1,1). Now:", circle3)
    print("Result of circle1.intersects(circle3) is: {}".format(circle1.intersects(circle3)))
    circle4 = Circle(1.0, 23.0, 1.5)
    circle5 = Circle(1.0, 23.0, 0.1)
    print("Sorted circles: ", sorted([circle1, circle2, circle3, circle4, circle5]))
