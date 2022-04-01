import sys
import os
from tkinter import *
from tkinter import messagebox

#CounterPhase is to control the phase of the program
#CounterPhase = 0 is default setting with no output
#CounterPhase = 1 is to create new coordinates
#CounterPhase = 2 is to use existing coordinates from a .txt file
counterPhase = 0

#onClick command
def onclick(number):
        window1.destroy()
        counterPhase = number
        if counterPhase == 1: #New coordinates
            import CreatingFileGUI

        if counterPhase == 2:#Existing coordinates
            import UseExistingFileGUI

window1=Tk()#First Window
window1.title('Selection')
window1.geometry("400x150")

window1Question = Label(window1, text="Do you wish to create or use existing coordinates?", font=(20))
window1Question.pack()

button1 = Button(window1,text = "Create",command=lambda:onclick(1))#Button to create new coordinates
button1.pack()
button2 = Button(window1,text = "Use Existing",command=lambda:onclick(2))#Button to use existing coordinates
button2.pack()
window1.mainloop()
