def q1(n):
    if n == 0:
        return [1]
    else:
        return q1(n-1) +[(n+1)*(n+1)] +q1(n-1) 
        
    
def q2(listOfStrings, n):
    if len(listOfStrings) == 1:
        if len(listOfStrings[0]) > n:
            return 1
        else:
            return 0
    else:
        #print(listOfStrings[:1], listOfStrings[1:])
        return q2(listOfStrings[:1], n) + q2(listOfStrings[1:], n)


def q3(item1, item2):
    #if len(item1) == 1:
    if type(item1) != list and type(item2) != list:
        if type(item1) == int:
            item1 = float(item1)
        if type(item2) == int:
            item2 = float(item2)
        if type(item1) == type(item2):
            return True
        else:
            return False
    elif type(item1) != type(item2):
        return False
    if len(item1) == len(item2):
        for i in range(len(item2)):
            #print(item1[i], item2[i])
            if not q3(item1[i], item2[i]):
                return False
        return True
    return False


def q4(inString):
    result = []
    if len(inString) == 1:
        return [inString]
    else:
        insert = inString[0]
        newList = q4(inString[1:])
        #print('newList =', newList)
        for index in range(len(newList)):
            #print('index =', index)
            word = newList[index]
            #print('word =', word)
            for n in range(len(word)+1):
                #print('insert =', insert)
                newWord = word[:n] + insert + word[n:]
                #print('newWord =', newWord)
                result = result + [newWord]
        return result
