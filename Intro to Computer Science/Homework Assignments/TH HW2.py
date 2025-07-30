def q1(origString, charsToReplace, count):
    result = ""
    index = 0
    while index < len(origString):
        currentChar = origString[index]
        if (currentChar in charsToReplace) or (currentChar in charsToReplace.upper()):
            result = result + (currentChar * count)
        else:
            result = result + currentChar
        index = index + 1
    return result

def q2(minLetter, inputString):
    smallestLetter = None
    smallestIndex = None
    secondSmallest = None
    secondSmallestIndex = None
    thirdSmallest = None
    thirdSmallestIndex = None
    mostCommon = None
    mostCommonTimes = None
    inputString = inputString.lower()
    index = 0

    while index < len(inputString):
        currentChar = inputString[index]
        
        if currentChar >= minLetter:
            if (smallestLetter == None) or (currentChar < smallestLetter):
                thirdSmallest = secondSmallest#
                thirdSmallestIndex = secondSmallestIndex#
                secondSmallest = smallestLetter#
                secondSmallestIndex = smallestIndex
                smallestLetter = currentChar
                smallestIndex = index
                
        if smallestLetter != None:
            if currentChar > smallestLetter:
                if (secondSmallest == None) or (currentChar < secondSmallest):
                    thirdSmallest = secondSmallest#
                    thirdSmallestIndex = secondSmallestIndex#
                    secondSmallest = currentChar
                    secondSmallestIndex = index
        if secondSmallest != None:
            if (currentChar > secondSmallest):
                if (thirdSmallest == None) or (currentChar < thirdSmallest):
                    thirdSmallest = currentChar
                    thirdSmallestIndex = index

        #print("Smallest is", smallestLetter)#
        #print("Second smallest is", secondSmallest)#
        #print("Third smallest is", thirdSmallest)#
        #print("Smallest index is", smallestIndex)#
        #print("Second smallest index is", secondSmallestIndex)#
        #print("Third smallest index is", thirdSmallestIndex)#
        index = index + 1

    index = 0
    while index < len(inputString):
        currentChar = inputString[index]
        def howMany(character, inputString):
            count = 0
            index = 0
            while index < len(inputString):
                currentChar = inputString[index]
                if character == currentChar:
                    count = count + 1
                    #print(character, "count + 1")
                
                index = index + 1
            return count, character
        
        count, character = howMany(currentChar, inputString)

        if (mostCommonTimes == None) or (count > mostCommonTimes):
            mostCommonTimes = count
            mostCommon = character
        
        index = index + 1
    
    return smallestLetter, smallestIndex, thirdSmallest, thirdSmallestIndex, mostCommon, mostCommonTimes

def q3(string1, string2):
    if len(string1) == len(string2):
        errors = 0
        index = 0
        while index < len(string1):
            curr1 = string1[index]
            curr2 = string2[index]
            if curr1 != curr2:
                errors = errors + 1
                #print("+1 error")
            #else:
                #print("same letter")
            if errors > 1:
                return False

            index = index + 1
        if errors == 1:
            return True
    else: return False

    return

def q4(string1, string2):

    listSame = []
    index = 0

    if len(string1) < len(string2):
        whileTimes = len(string1)
    else:
        whileTimes = len(string2)
    
    while index < whileTimes:
        curr1 = string1[index]
        curr2 = string2[index]
        if curr1 == curr2:
            listSame = listSame + [index]

        index = index + 1
        

    return listSame







