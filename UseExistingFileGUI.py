from tkinter import *
from tkinter import messagebox
import Tkinter
import os
import sys
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    
def extractingCoordinateValue(number):
    coordinateValue = []
    dataTxtSelected = open("Bin"+number+".txt", "r")
    for line in dataTxtSelected:
        coordinateValue.append(int(line))
    return coordinateValue

def binCoordinate(coordinate, lineValue):
    position = coordinate[lineValue]
    return position

def checkingIfFileExistance(number):
        dataTxtSelected = open("Bin"+number+".txt", "r")
        return number

def tempFiling(binNumber,x,y):
    tempFile = open("TempFile.txt","w")
    tempFile.write(str(binNumber)+'\n')
    tempFile.write(str(x)+'\n')
    tempFile.write(str(y))
    tempFile.close()

def onClick3():
    try:
        binNumber = checkingIfFileExistance(binNumberEx.get())
        windowEx.destroy()
        txtFile = extractingCoordinateValue(binNumberEx.get())
        xPosition = binCoordinate(txtFile, 0)
        yPosition = binCoordinate(txtFile, 1)
        tempFile = tempFiling(binNumber, xPosition, yPosition)
    except IOError:
        messagebox.showerror(title='Error',message="Invalid. File does not exist")

windowEx=Tk()
windowEx.title("Bin Number")
windowEx.geometry("400x150")

labelwindowEx=Label(windowEx,text="Specify bin number: ",font=(14))
labelwindowEx.pack()

binNumberEx = StringVar()

binNumberInput = Entry(windowEx,textvariable=binNumberEx,font=(14))
binNumberInput.pack()

buttonE1 = Button(windowEx, text="Confirm",font=(14),command=onClick3)
buttonE1.pack()

windowEx.mainloop()
