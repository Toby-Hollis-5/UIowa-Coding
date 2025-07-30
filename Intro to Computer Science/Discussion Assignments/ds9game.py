import tkinter
import random

# This code implements an annoying-to-play number guessing game.  In this DS
# assignment your job will be to make several changes that will make the game better.
#
# It uses many global variables, which is usually not good practice but is a quick way to get
# started learning tkinter/GUI programming.

# TO RUN THIS:
# 1) load into python.
# 2) type startGameGUI(6)    (or some number other than 6)
#     in the Python interpreter
# 3) after that, you can enter a number into the form in the window and click the Check It! button
#    to see if that's the right number
#

# Randomly choose number in between 1 and maxPossibleValue (inclusive)
# as the number to be guessed by the player.
# Also: set window title to indicate player should guess between 1 and that max 
#       set status lable to indicate no guesses have been made yet
#       set button text to say "Check It!"
#
def initializeGame(maxPossibleValue):
    global numberToGuess
    global maxNumberToBeGuessed
    maxNumberToBeGuessed = maxPossibleValue
    numberToGuess = random.randint(1,maxPossibleValue)
    gameWindow.title("Guess number between 1 and {}".format(maxNumberToBeGuessed))
    statusLabel.configure(text="You haven't made any guesses yet")
    button1.configure(text="Check It!", command=checkGuess)

# Read number entered into GUI by player, check whether it's correct, and
# give appropriate feedback in the statusLabel
#
def checkGuess():
    global numberToGuess
    guessAsString = guessEntry.get()
    guess = int(guessAsString)
    if guess == numberToGuess:
        statusLabel.configure(text = str(guess) + " is it - you win!")
        button1.configure(text = "New game", command = newGame)
    elif guess > numberToGuess:
        statusLabel.configure(text = str(guess) + " is too high. Try again.")
    else:
        statusLabel.configure(text = str(guess) + " is too low. Try again.")

    guessEntry.delete(0, tkinter.END)

# Global variables 

# The maximum number that can be chosen as the number to be guessed.
# As part of initializing a game, generateAndSetNumberToGuess chooses a
# random integer in the interval  [1, maxNumToBeGuessed] as the number the
# that the player needs to guess.
maxNumberToBeGuessed = None

# During a game, the number that is to be guessed
numberToGuess = None

# The main window, where interaction and feedback will occur
gameWindow = None

# The only button in the GUI
button1 = None

def initializeGameWindow():
    global gameWindow
    global guessEntry
    global statusLabel
    global button1
    
    gameWindow = tkinter.Tk()
    
    # topFrame is a container to hold three widgets in the top row of the window
    # 1) a label, 2) an Entry, where users can type guesses, 3) a button to press
    topFrame = tkinter.Frame(gameWindow)
    topFrame.pack()

    label1 = tkinter.Label(topFrame, text="Your guess:")
    label1.pack(side=tkinter.LEFT)
    guessEntry = tkinter.Entry(topFrame)
    guessEntry.pack(side=tkinter.LEFT)
    button1 = tkinter.Button(topFrame, text="Check It!", command=checkGuess)
    button1.pack()

    # create and place a Label below the topFrame container. Messages about
    # game status will be shown on this label.
    statusLabel = tkinter.Label(gameWindow, text="You haven't made any guesses yet")
    statusLabel.pack()

# Call this function to start the GUI and game!
#
def startGameGUI(maxNumberToBeGuessed):
    global numberToGuess
    initializeGameWindow()
    initializeGame(maxNumberToBeGuessed)
    gameWindow.mainloop()

def newGame():
    initializeGame(maxNumberToBeGuessed)
