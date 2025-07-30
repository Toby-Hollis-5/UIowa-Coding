class FastList:
    def __init__(self):
        self.items = []
        self.currLen = 0
        self.currMax = None
        self.currMin = None
        self.currSum = 0

    def getMax(self):
        return self.currMax

    def getMin(self):
        return self.currMin

    def getAverage(self):
        return self.currSum / self.currLen

    # add number to list, updating other properties as needed.
    def addOn(self, number):
        self.items.append(number)
        if self.currMax == None or number > self.currMax:
            self.currMax = number
        if self.currMin == None or number < self.currMin:
            self.currMin = number
        self.currSum = self.currSum + number
        self.currLen = self.currLen + 1

    #def append(self, number):
        #self.addOn(number)

def testFastList():
    l = FastList()
    l.append(5)
    print(l.getMax())
    print(l.getMin())
    print(l.getAverage())
    l.addOn(100)
    l.addOn(45)
    print(l.getMax())
    print(l.getMin())
    print(l.getAverage())
    l.addOn(300)
    print(l.getMax())
    print(l.getMin())
    print(l.getAverage())
