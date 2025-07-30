import tkinter
import random

mainWindow = tkinter.Tk()

def guessCheck():
    global count, answer, problemsSolved
    #Check if the inputted number is the solution to the given problem.
    textInEntry = textEntry.get()
    textEntry.delete(0, tkinter.END)
    count = count + 1
    if textInEntry == str(answer):
        feedbackLabel.configure(text="Correct!")
        textEntry.config(state='disabled')
        countList.append(count)
        problemsSolved = problemsSolved + 1
    else:
        feedbackLabel.configure(text="Incorrect.")

    countLabel.configure(text="Number of guesses: {}".format(count))

    return count

countList = []
problemsAttempted = 1
problemsSolved = 0

def newProblem():
    global problemType, globalType, answer, problemsAttempted, count
    #print('problem type=', problemType, 'globalType =', globalType)
    
    if globalType == "anything":
        problemType, globalType = anything()
    
    firstOp, secondOp, answer = generateProblem()

    questionLabel.configure(text="What is {} {} {}?".format(firstOp, problemType, secondOp))
    textEntry.config(state='normal')

    problemsAttempted = problemsAttempted + 1
    count = 0
    countLabel.configure(text="Number of guesses: {}".format(count))

def multiplication():
    global problemType, globalType
    problemType = "*"
    globalType = "*"
    problemTypeLabel.configure(text="Current problem type: {}".format(globalType))

def addition():
    global problemType, globalType
    problemType = "+"
    globalType = "+"
    problemTypeLabel.configure(text="Current problem type: {}".format(globalType))

def subtraction():
    global problemType, globalType
    problemType = "-"
    globalType = "-"
    problemTypeLabel.configure(text="Current problem type: {}".format(globalType))

def division():
    global problemType, globalType
    problemType = "/"
    globalType = "/"
    problemTypeLabel.configure(text="Current problem type: {}".format(globalType))

def anything():
    global problemType, globalType

    if globalType != None:
        problemTypeLabel.configure(text="Current problem type: anything")
    
    problemFind = random.randrange(0, 4)
    if problemFind == 0:
        problemType = "*"
    elif problemFind == 1:
        problemType = "+"
    elif problemFind == 2:
        problemType = "-"
    else:
        problemType = "/"
    globalType = "anything"
    return problemType, globalType



problemsList = []

def generateProblem():
    
    if problemType == "+" or problemType == "-" or problemType == "/":
        #If problem is +, -, or /:
        firstOp = random.randrange(0, 1000)
        #print(firstOp)
        if problemType == "+":
            secondOp = random.randrange(0, 1000)
            answer = firstOp + secondOp
        elif problemType == "-":
            secondOp = random.randrange(0, firstOp+1)
            answer = firstOp - secondOp
        else:
            #problemType == "/"
            divisorList = []
            for num in range(1, firstOp+1):
                divisorList.append(num)

            divisorList.reverse()
            worksList = []

            for num in divisorList:
                if firstOp / num == firstOp // num:
                    worksList.append(num)

            print('worksList =', worksList)

            secondOp = random.choice(worksList)
            answer = int(firstOp / secondOp)
        
    else:
        #Else, multiplication:
        firstOp = random.randrange(0, 100)
        secondOp = random.randrange(0, 100)
        answer = firstOp * secondOp

    for problem in problemsList:
        if [firstOp, problemType, secondOp] == problem:
            firstOp, secondOp, answer = generateProblem()
            #print("same")

    problemsList.append([firstOp, problemType, secondOp])

    #print('answer=', answer)

    return firstOp, secondOp, answer

def endGame():
    countSum = 0
    for num in countList:
        countSum = countSum + num

    

    avg = countSum / problemsAttempted

    print('Problems attempted:', problemsAttempted)
    print('Problems solved:', problemsSolved)
    print('Average number of total guesses:', avg)
    
    mainWindow.destroy()

globalType = None
problemType, globalType = anything()
firstOp, secondOp, answer = generateProblem()
count = 0

questionContainer = tkinter.Frame(mainWindow)
questionContainer.pack()

questionLabel = tkinter.Label(questionContainer, text="What is {} {} {}?".format(firstOp, problemType, secondOp))
questionLabel.pack(side=tkinter.LEFT)
textEntry = tkinter.Entry(questionContainer)
textEntry.pack()

answerContainer = tkinter.Frame(mainWindow)
answerContainer.pack()

countLabel = tkinter.Label(answerContainer, text="Number of guesses: {}".format(0))
countLabel.pack(side=tkinter.LEFT)

button = tkinter.Button(answerContainer, text="Check guess", command=guessCheck)
button.pack(side=tkinter.LEFT)

feedbackLabel = tkinter.Label(answerContainer)
feedbackLabel.pack(side=tkinter.LEFT)

problemTypeButtonsContainer = tkinter.Frame(mainWindow)
problemTypeButtonsContainer.pack()

additionButton = tkinter.Button(problemTypeButtonsContainer, text = "Addition", command=addition)
additionButton.pack(side=tkinter.LEFT)
subtractionButton = tkinter.Button(problemTypeButtonsContainer, text = "Subtraction", command=subtraction)
subtractionButton.pack(side=tkinter.LEFT)
multiplicationButton = tkinter.Button(problemTypeButtonsContainer, text = "Multiplication", command=multiplication)
multiplicationButton.pack(side=tkinter.LEFT)
divisionButton = tkinter.Button(problemTypeButtonsContainer, text = "Division", command=division)
divisionButton.pack(side=tkinter.LEFT)
anythingButton = tkinter.Button(problemTypeButtonsContainer, text = "Anything", command=anything)
anythingButton.pack(side=tkinter.LEFT)
newProblemButton = tkinter.Button(problemTypeButtonsContainer, text = "New problem", command=newProblem)
newProblemButton.pack(side=tkinter.LEFT)

problemTypeLabelContainer = tkinter.Frame(mainWindow)
problemTypeLabelContainer.pack()

problemTypeLabel = tkinter.Label(problemTypeLabelContainer, text = "Current problem type: {}".format(globalType))
problemTypeLabel.pack()

endButton = tkinter.Button(problemTypeLabelContainer, text="End Game", command=endGame)
endButton.pack()



mainWindow.mainloop()
