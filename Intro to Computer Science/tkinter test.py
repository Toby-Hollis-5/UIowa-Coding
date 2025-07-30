import tkinter
#from tkinter import Button, Entry, END, Frame, Label, Tk, LEFT

# callback functions

def buttonPushed():
    textInEntry = textEntry.get()
    textEntry.delete(0, END)
    print(textInEntry)

# Create main window
mainWindow = Tk()

# Create a Frame (called 'container') to hold two side-by-side widgets, the label and the entry
container = Frame(mainWindow)
container.pack()
                  
label = Label(container, text="Enter some text:")
label.pack(side=LEFT)
textEntry = Entry(container)
textEntry.pack()

# Create a button and put it beneath the container.
# Specify buttonPushed as "callback" function that gets called when the button is pressed.
button = Button(mainWindow, text="Print entry text in shell", command=buttonPushed)
button.pack()

# GO!
mainWindow.mainloop()
