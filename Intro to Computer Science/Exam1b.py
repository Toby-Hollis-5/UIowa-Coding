def q4(listOfStrings1, listOfStrings2):
    result = []
    index = 0

    if len(listOfStrings1) < len(listOfStrings2):
        listLength = len(listOfStrings1)
    else:
        listLength = len(listOfStrings2)

    while index < listLength:
        item1 = listOfStrings1[index]
        item2 = listOfStrings2[index]

        if len(item1) == len(item2):
            result = result + [index]
        
        index = index + 1

    return result
