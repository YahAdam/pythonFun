from tkinter import *
import random
import os
from tkinter.ttk import *

window = Tk()

dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, 'dinnerOptions.txt') 

def pickOption():
    lines = open(filename).read().splitlines()
    selected = random.choice(lines)
    return picked.configure(text = selected)


def openNewWindow(): 
    def addOption(input):
        items = open(filename).read().splitlines()
        lowerItems = map(lambda x: x.lower(), items)
        with open(filename, "a") as my_file:
            if input == "":
                errorLabel.configure(text="Please enter something")
            elif input.lower() in lowerItems:
                errorLabel.configure(text=f'{input} is already in the list, try another')
            else:        
                addedLabel.configure(text=f'{input} has been added to the list!')
                my_file.write("\n" + input)

    addOptionWindow = Toplevel(window)
    addOptionWindow.title("Add Dinner Options")
    addOptionWindow.geometry('350x200')
    
    txt = Entry(addOptionWindow,width=20)
    addLabel = Label(addOptionWindow, text="Enter a new dinner option")
    errorLabel = Label(addOptionWindow)
    addedLabel = Label(addOptionWindow)
    addOptionButton = Button(addOptionWindow, text="Add Option", command= lambda: addOption(txt.get()))

    txt.grid(column=1, row =1)
    addLabel.grid(column=1, row=0)
    addOptionButton.grid(column=2, row=1)
    errorLabel.grid(column= 1, row=3)
    addedLabel.grid(column= 1, row=3)
     
window.geometry('350x200')
window.title("Dinner Picker")

btn = Button(window, text="What's for dinner?", style = 'W.TButton', command=pickOption)
picked = Label(window)
openAddWindow = Button(window, text="Add more dinner options", command=openNewWindow)
style = Style()
style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'),foreground = 'red')

btn.grid(column=1, row=3)
picked.grid(column=2,row=11)
openAddWindow.grid(column=2, row=12)

window.mainloop()
