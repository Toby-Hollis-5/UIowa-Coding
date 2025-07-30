def egypt(numerator, denominator):
    denomList = []
    originalNumerator = numerator
    originalDenominator = denominator

    candidate = 2
    while numerator != 0:
        if ((candidate * numerator) - denominator) >= 0:
            numerator = ((candidate * numerator) - denominator)
            denominator = candidate * denominator
            denomList.append(candidate)
            #print("next denom =", candidate)

        candidate = candidate + 1
    print("{}/{} =".format(originalNumerator, originalDenominator), end=" ")
    i = 0
    while i < len(denomList):
        curr = denomList[i]

        if curr == denomList[-1]:
            print("1/{}".format(curr))
        else:
            print("1/{} +".format(curr), end=" ")

        i = i + 1

    print(denomList)
