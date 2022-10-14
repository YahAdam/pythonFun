from tkinter import *
import random
import os

window = Tk()

dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, 'dinnerOptions.txt') 

def pickOption():
    lines = open(filename).read().splitlines()
    selected = random.choice(lines)
    return picked.configure(text=selected)

def addOption():
    file_object = open(filename, 'a')
    addedOption = txt.get()
    file_object.write("\n" + addedOption)
    file_object.close()
     
window.geometry('350x200')

window.title("Dinner Picker")

btn = Button(window, text="What's for dinner fam?", command=pickOption)

picked = Label(window)

#add options
txt = Entry(window,width=20)
addLabel = Label(window, text="Enter a new dinner option")
addOptionButton = Button(window, text="Add Option", command=addOption)

btn.grid(column=1, row=3)
picked.grid(column=2,row=11)
txt.grid(column=1, row =9)
addLabel.grid(column=1, row=8)
addOptionButton.grid(column=2, row=9)

window.mainloop()
