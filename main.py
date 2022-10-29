from tkinter import *
import random
import os

window = Tk()

dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, 'dinnerOptions.txt') 

def pickOption():
    lines = open(filename).read().splitlines()
    selected = random.choice(lines)
    return picked.configure(text = selected)


def openNewWindow(): 
    def addOption(input):
        file_object = open(filename, 'a')
        if input == "":
            errorLabel.configure(text="Please enter something")
            file_object.close()
        else:
            addedLabel.configure(text=f'{input} has been added to the list!')
            file_object.write("\n" + input)
            file_object.close()

    addOptionWindow = Toplevel(window)
    addOptionWindow.title("Add Dinner Options")
    addOptionWindow.geometry("200x200")
    txt = Entry(addOptionWindow,width=20)
    addLabel = Label(addOptionWindow, text="Enter a new dinner option")
    errorLabel = Label(addOptionWindow)
    addedLabel = Label(addOptionWindow)
    addOptionButton = Button(addOptionWindow, text="Add Option", command=addOption(txt.get()))

    txt.grid(column=1, row =1)
    addLabel.grid(column=1, row=0)
    addOptionButton.grid(column=2, row=1)
    errorLabel.grid(column= 1, row=3)
    addedLabel.grid(column= 1, row=3)
     
window.geometry('350x200')

window.title("Dinner Picker")

btn = Button(window, text="What's for dinner?", command=pickOption)

picked = Label(window)

#add options
openAddWindow = Button(window, text="Add more dinner options", command=openNewWindow)

btn.grid(column=1, row=3)
picked.grid(column=2,row=11)

openAddWindow.grid(column=2, row=12)

window.mainloop()
