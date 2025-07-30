def q1(n):
    if n % 14 == 0:
        print(n, "is a multiple of 14")
    elif n % 7 == 0:
        print(n, "is a multiple of 7")
    elif n % 2 == 0:
        print(n, "is a multiple of 2")
    else:
        print(n, "is not a multiple of 2, 7, or 14")
    return

def q2(n):
    currentNumber = 1
    while currentNumber <= n:
        q1(currentNumber)
        currentNumber = currentNumber + 1
    return

def printDigitsOf(n):
    newNumber = n
    while not newNumber == 0:
        lastDigit = newNumber % 10
        print(lastDigit)

        newNumber = newNumber // 10

    return

def sumDigitsOf(n):
    newNumber = n
    result = 0
    while not newNumber == 0:
        lastDigit = newNumber % 10
        result = result + lastDigit

        newNumber = newNumber // 10

    return result

