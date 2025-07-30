# CS 1210, Fall 2020
# Discussion section 6, Oct. 20-22.  Due 5pm Oct. 22

# DISCUSSION SECTION WORK:
#

# Download this file, ds6.py and also stack.py and circle.py
#
# 1. After studying the Stack class and testStack() functions in stack.py
#    complete the Queue class below (and test it with the testQueue function)
#
# 2. Afer studying and testing the Circle class in circle.py,
#    complete the Rectangle class below (and test it with
#    the testRectangle function)
#
# 3. SUBMIT THIS ONE FILE, with your updates, TO ICON.
#
#
# NOTE: you may certainly add more tests to the test functions if you want!!

#####

# 1. Complete the Queue class (following the style of the Stack class)
#
# A queue is similar to a stack but a bit different.
#
# A queue is a collection of items supporting three operations:
#   - enqueue (item): add item to the "front" of the queue
#   - dequeue(): removes the "last" item from the queue
#                 (the one that's been in the queue the longest) and returns it
#   - size(): returns the number of items currently in the queue
#
# Note: stacks are "LIFO" (last-in-first-out)
#       while queues are "FIFO" (first-in-first-out)

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return(len(self.items) == 0)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not(self.isEmpty()):
            first = self.items.pop(0)
            return first
        else:
            print("Error: you can't pop anything from an empty queue")

    def size(self):
        return len(self.items)

def testQueue():
    q = Queue()
    print("Created an empty Queue")
    print("Size is now: {}".format(q.size()))
    print("Enqueue-ing: 3, then 'hi', then 99")
    q.enqueue(3)
    q.enqueue("hi")
    q.enqueue(99)
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print("Size is now: {}".format(q.size()))
    print("Enqueue-ing: [1,2]")
    q.enqueue([1,2])
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print("Size is now: {}".format(q.size()))
    print(q.dequeue())
    print("Size is now: {}".format(q.size()))


# 2. Complete the Rectangle class (following the style of the Circle class) 

import math

class Rectangle:
    def __init__(self, centerX = 0.0, centerY = 0.0, width = 0.0, height = 0.0):
        self.centerX = centerX
        self.centerY = centerY
        self.width = width
        self.height = height
    
    def __repr__(self):
        return "< rectangle with width {} and height {} centered at ({},{}) >".format(self.width, self.height, self.centerX, self.centerY)
       
    def setCenter(self, x, y):
        self.centerX = x
        self.centerY = y
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
   
    #
    # the intersects method should return True if the two rectangles
    # touch/intersect at all (even they just touch exactly at their edges or
    # corners). Note: think carefully about how to do this test. Sketching
    # some pictures can help you analyze the possibilities.
    #
    def intersects(self, otherRectangle):
        distanceBetweenX = abs(self.centerX - otherRectangle.centerX)
        #print('distanceBetweenX =', distanceBetweenX)
        distanceBetweenY = abs(self.centerY - otherRectangle.centerY)
        #print('distanceBetweenY =', distanceBetweenY)
        if (self.width/2 + otherRectangle.width/2) >= distanceBetweenX:
            if (self.height/2 + otherRectangle.height/2) >= distanceBetweenY:
                return True
        return False

def testRectangle():
  rect1 = Rectangle(10.0, 5.0, 2.0, 1.0)
  print("Rectangle 1:", rect1)
  print("  area:", rect1.area(), "perimeter:", rect1.perimeter())
  rect2 = Rectangle(0, 0, 3.5, 2.5)
  print("Rectangle 2:", rect2)
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  rect1.setCenter(2.75, 0.0)
  print("After setting center of Rectangle 1 to (2.75, 0.0)")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  rect1.setCenter(2.76, 0.0)
  print("After setting center of Rectangle 1 to (2.76, 0.0)")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  rect1.setCenter(-2.75, 1.75)
  print("After setting center of Rectangle 1 to (-2.75, 1.75)")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  print("After setting center of Rectangle 1 to (0,0)")
  rect1.setCenter(0.0, 0.0)
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  rect1.setCenter(10.0,0)
  print("After setting center of Rectangle 1 to (10.0, 0.0)")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))   
  rect1.setWidth(20.0)  
  print("After setting width of Rectangle 1 to 20.0")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
  rect1.setCenter(0,-10)
  print("After setting center of Rectangle 1 to (0, -10.0)")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))   
  rect1.setHeight(17.5)  
  print("After setting height of Rectangle 1 to 17.5")
  print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))    
