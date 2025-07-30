def q3(listOfLists, vLow, vHigh):
    numLists = 0
    maxList = []
    for item in listOfLists:

        maxNum = None
        currListMid = 0
    
        for sub in item:
            
            if sub > vLow and sub < vHigh and currListMid == 0:
                numLists = numLists + 1
                currListMid = currListMid + 1
            
            if maxNum == None or sub > maxNum:
                maxNum = sub
                #print(maxNum)

        maxList.append(maxNum)

    return numLists, maxList
