import random

class Box:
    
    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth
        
    def __repr__(self):
        return "< {}-by-{}-by-{} 3D box with center at ({},{},{}) >".format(self.width, self.height, self.depth, self.centerX, self.centerY, self.centerZ)
    
    def setCenter(self, x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
        
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height
        
    def setDepth(self, depth):
        self.depth = depth
    
    def volume(self):
        return self.width * self.height * self.depth
    
    def surfaceArea(self):
        return (2 * (self.height * self.width)) + (2 * (self.height * self.depth)) + (2 * (self.width * self.depth))
    
    def overlaps(self, otherBox):
        
        distanceBetweenX = abs(self.centerX - otherBox.centerX)
        distanceBetweenY = abs(self.centerY - otherBox.centerY)
        distanceBetweenZ = abs(self.centerZ - otherBox.centerZ)
        
        if self.width/2 + otherBox.width/2 >= distanceBetweenX:
            if self.height/2 + otherBox.width/2 >= distanceBetweenY:
                if self.depth/2 + otherBox.depth/2 >= distanceBetweenZ:
                    return True
        
        return False
    
    def isInside(self, otherBox):
        
        maxWidthPointSelf = self.centerX + self.width/2
        minWidthPointSelf = self.centerX - self.width/2
        maxHeightPointSelf = self.centerY + self.height/2
        minHeightPointSelf = self.centerY - self.height/2
        maxDepthPointSelf = self.centerZ + self.depth/2
        minDepthPointSelf = self.centerZ - self.depth/2
        
        maxWidthPointOther = otherBox.centerX + otherBox.width/2
        minWidthPointOther = otherBox.centerX - otherBox.width/2
        maxHeightPointOther = otherBox.centerY + otherBox.height/2
        minHeightPointOther = otherBox.centerY - otherBox.height/2
        maxDepthPointOther = otherBox.centerZ + otherBox.depth/2
        minDepthPointOther = otherBox.centerZ - otherBox.depth/2
        
        #if max point of box1 is less than max point of box2 and min point of box1 is greater than min point of box2:
        if maxWidthPointSelf < maxWidthPointOther and minWidthPointSelf > minWidthPointOther:
            if maxHeightPointSelf < maxHeightPointOther and minHeightPointSelf > minHeightPointOther:
                if maxDepthPointSelf < maxDepthPointOther and minDepthPointSelf > minDepthPointOther:
                    return True
        
        return False
    
    
class NimGame:
    
    def __init__(self, initList):
        self.heaps = initList
        print("Nim game initialized with {} heaps.".format(len(self.heaps)))
        
    def __repr__(self):
        print("< Nim game with {} heaps. ".format(len(self.heaps)))
        index = 0
        while index < len(self.heaps):
            curr = self.heaps[index]
            if curr == 1:
                print("\t Heap {}: {} ball".format(index, curr))
            else:
                print("\t Heap {}: {} balls".format(index, curr))
            index = index + 1

        return '>'
            
    def remove(self, number, heap):
        
        if self.heaps[heap] - number < 0:
            return "You can't take that many balls from heap {}. Try again.".format(heap)
        
        #print('heap before removal =', self.heaps[heap])
        self.heaps[heap] = self.heaps[heap] - number
        #print('heap after removal =', self.heaps[heap])
        
        if number == 1:
            print("You took {} ball from heap {}.".format(number, heap))
        else:
            print("You took {} balls from heap {}.".format(number, heap))
        
        if self.gameOver() == True:
            return "You win!"
        
        heapsAvailable = []
        index = 0
        while index < len(self.heaps):
            if self.heaps[index] != 0:
                heapsAvailable.append(index)
                
            index = index + 1
        
        #print('heapsAvailable =', heapsAvailable)
                
        compHeap = random.choice(heapsAvailable)
        #print('compHeap =', compHeap)
        compNum = random.randint(1, self.heaps[compHeap])
        #print('compNum =', compNum)
        
        self.heaps[compHeap] = self.heaps[compHeap] - compNum
        
        if compNum == 1:
            print("Computer took {} ball from heap {}.".format(compNum, compHeap))
        else:
            print("Computer took {} balls from heap {}.".format(compNum, compHeap))
        
        
        if self.gameOver() == True:
            return "Computer wins!"
        
        #print('game so far=', self.heaps)
    
    def gameOver(self):
        for item in self.heaps:
            if item > 0:
                return False
        
        return True
        
class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)

class Cow(Animal):
    def __init__(self, name = 'bessy'):
        Animal.__init__(self, name, 4)

    def speak(self):
        print('moo')

    def milk(self):
        print('Milking...')

    def __repr__(self):
        return '<{} the cow. ID:{}>'.format(self.name, self.id)

        
def testAnimal():
    c1 = Cat("Milo")
    c2 = Cat(furColor = "black")
    d1 = Dog()
    d2 = Dog()
    for animal in [c1, c2, d1, d2]:
        print(animal)
        animal.speak()
    d1.fetch()
    print(c2.getFurColor())
