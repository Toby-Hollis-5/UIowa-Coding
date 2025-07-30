def q1w(inputString, inputDict, specialValue):
    s = 0
    s2 = 0
    a = 0.0
    index = 0
    while index < len(inputString):
        char = inputString[index]
        s = s + inputDict[char]
        if inputDict[char] == specialValue:
            s2 = s2 + 1
        index = index + 1
    a = s / len(inputString)
    return (a, s2)
