def q1(L, goalX, goalY):
    minX = None
    minY = None
    for numberList in range(len(L)):
        #print("numberList =", numberList)
        if minX == None or (abs(L[numberList][0] - goalX) < minXDif):
            #print(abs(L[numberList][0] - goalX), "is less than", minX)
            minX = L[numberList][0]
            minXDif = abs(L[numberList][0] - goalX)
            #print(abs(L[numberList][0] - goalX))
            #print("minX =", minX)
            minXnumberList = numberList
        #else:
            #print(L[numberList], "isn't a better minX")
        if minY == None or (abs(L[numberList][1] - goalY) < minY):
            minY = L[numberList][1]
            minYDif = abs(L[numberList][1] - goalY)
            #print(abs(L[numberList][1] - goalY))
            #print("minY =", minY)
            minYnumberList = numberList
        #else:
            #print(L[numberList], "isn't a better minY")
        #if
    #print("minX =", minX)
    #print("minY =", minY)
    #print("minXDif =", minXDif)
    #print("minYDif =", minYDif)

    if minXDif < minYDif:
        return ((L[minXnumberList]), "x")
    else:
        return ((L[minYnumberList]), "y")

    return
    


#q1([[10, 25], [2, 2], [49, 200]], 50, 8)
#q1([[49, 200], [2, 2], [10, 25]], 50, 8)


def q2(L):
    sumList = []
    positiveNumsList = 0
    minValue = None
    for numberList in range(len(L)):
        #print(L[numberList])
        sumListNumber = 0
        positiveNums = 0
        negativeNums = 0
        for numberSub in range(len(L[numberList])):
            currNum = L[numberList][numberSub]
            sumListNumber = sumListNumber + currNum
            
            if minValue == None or currNum < minValue:
                minValue = currNum
            
            if currNum > 0:
                positiveNums = positiveNums + 1
            elif currNum < 0:
                negativeNums = negativeNums + 1
            
            

        sumList.append(sumListNumber)
        
        if positiveNums > negativeNums:
            positiveNumsList = positiveNumsList + 1
        

    return [sumList, positiveNumsList, minValue]
    

def q3(listOfLists, infoDict):
    returnList = []
    for numberList in range(len(listOfLists)):
        currentList = []
        currentList = currentList + listOfLists[numberList][:]
        currentList.sort()
        #print(currentList)
        numBlue = 0
        numRed = 0
        numGreen = 0
        largestOfList = None
        smallestOfList = None
        mostCommonOfList = None
        count = 0
        greatestCount = 0


        for numberSub in range(len(currentList)):
            currSub = currentList[numberSub]
            #print("currSub =", currSub)
            
            if currSub in infoDict:
                #print(currSub, "is in dict")
                if infoDict[currSub] == "blue":
                    #print(currSub, "is blue")
                    numBlue = numBlue + 1
                elif infoDict [currSub] == "red":
                    #print(currSub, "is red")
                    numRed = numRed + 1
                else:
                    #print(currSub, "is green")
                    numGreen = numGreen + 1
            else:
                #print(currSub, "is not in dict")
                numGreen = numGreen + 1

            if largestOfList == None or currSub > largestOfList:
                #print("largest =", currSub)
                largestOfList = currSub
            if smallestOfList == None or currSub < smallestOfList:
                #print("smallest =", currSub)
                smallestOfList = currSub

            if count == 0 or currSub == (currentList[numberSub-1]):
                #print("same as last, count + 1")
                count = count + 1
            else:
                #print("reset count to 1")
                count = 1
            if mostCommonOfList == None or count > greatestCount:
                greatestCount = count
                mostCommonOfList = currSub
            #print("count =", count)
            #print("most common =", mostCommonOfList)
                
        #print("numRed =", numRed)
        #print("numBlue =", numBlue)
        #print("numGreen =", numGreen)
        #print("most common =", mostCommonOfList)
        

        
        if numRed > numBlue:
            #print("added Red ...", smallestOfList)
            returnList.append(smallestOfList)
        elif numBlue > numRed:
            #print("added Blue ...", largestOfList)
            returnList.append(largestOfList)
        elif numGreen > numBlue and numGreen > numRed:
            returnList.append(mostCommonOfList)
        else:
            #print("added green ...", mostCommonOfList)
            returnList.append(mostCommonOfList)

        
    return returnList
