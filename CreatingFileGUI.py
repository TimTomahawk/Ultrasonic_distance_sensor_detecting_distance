import sys
import os
from tkinter import *

from tkinter import messagebox

xPosition = 0
yPosition = 0
windowNew=Tk()
windowNew.title("Bin Number")
windowNew.geometry("400x150")


def createNewFile(binNumber,x,y):
    newTxtFile = open("Bin"+str(binNumber)+".txt","w")
    newTxtFile.write(str(x)+'\n')
    newTxtFile.write(str(y))
    newTxtFile.close()
    tempFile = open("TempFile.txt","w")
    tempFile.write(str(binNumber)+'\n')
    tempFile.write(str(x)+'\n')
    tempFile.write(str(y))
    tempFile.close()

def coordinateCheck (x,y):
    xPosition = int(x)
    yPosition = int(y)
    return xPosition, yPosition

def onClick():
    try:
        confirmNumberForBin = int(binNumber.get())
        windowNew.destroy()
        windowNewPos=Tk()
        windowNewPos.title("Coordinates")
        windowNewPos.geometry("400x150")

        def onClick2():
            try:
                gettingCoordinates = coordinateCheck(xPos.get(),yPos.get())
                windowNewPos.destroy()
                creatingFile = createNewFile(confirmNumberForBin,gettingCoordinates[0],gettingCoordinates[1])
            except:
                messagebox.showerror(title='Error',message="Invalid Coordinates, try again")

        labelwindowNewPos1=Label(windowNewPos,text="Enter a X Position: ",font=(14))
        labelwindowNewPos1.pack()

        xPos = StringVar()

        xPosQ = Entry(windowNewPos,textvariable=xPos,font=(14))
        xPosQ.pack()

        labelwindowNewPos2=Label(windowNewPos,text="Enter a Y Position: ",font=(14))
        labelwindowNewPos2.pack()

        yPos = StringVar()

        yPosQ = Entry(windowNewPos,textvariable=yPos,font=(14))
        yPosQ.pack()

        buttonN11 = Button(windowNewPos,text="Confirm",font=(14),command=onClick2)
        buttonN11.pack()
        windowNewPos.mainloop()
    except:
        messagebox.showerror(title='Error',message="Please pick an integer")

labelwindowNew=Label(windowNew,text="Specify bin number: ",font=(14))
labelwindowNew.pack()

binNumber = StringVar()

binNumberInput = Entry(windowNew,textvariable=binNumber,font=(14))
binNumberInput.pack()

buttonN1 = Button(windowNew, text="Confirm",font=(14),command=onClick)
buttonN1.pack()

windowNew.mainloop()
