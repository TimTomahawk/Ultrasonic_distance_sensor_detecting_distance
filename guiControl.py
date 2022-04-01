import sys
import os
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import tkinter as tk

motorSpeed1 = 0
motorSpeed2 = 0
motorSpeed3 = 0
motorSpeed4 = 0

windowNew = tk.Tk()
windowNew.title("Control System")
windowNew.geometry("320x150")

def onClickStop():
  motorSpeed1 = 0
  motorSpeed2 = 0
  motorSpeed3 = 0
  motorSpeed4 = 0
  messagebox.showinfo(title='Action: Stop',message="The robot has stopped!")
  if askyesno(title ='Question', message ="Do you wish to continue?"):
      print(motorSpeed1)
      print(motorSpeed2)
      print(motorSpeed3)
      print(motorSpeed4)
  else:
     messagebox.showinfo(title='Action: End',message="End System")
     sys.exit()


def onClickStart():
  motorSpeed1 = 1
  motorSpeed2 = 1
  motorSpeed3 = 1
  motorSpeed4 = 1
  messagebox.showinfo(title='Action: Start',message="The robot is moving to position!")
  print(motorSpeed1)
  print(motorSpeed2)
  print(motorSpeed3)
  print(motorSpeed4)



labelwindowNew=tk.Label(windowNew,text="Control Display: ",font=(14))
labelwindowNew.pack(padx=5, pady=15,side=tk.LEFT)

buttonN1 = tk.Button(windowNew, text="Start",font=(14),command=onClickStart)
buttonN1.pack(padx=5, pady=20,side=tk.LEFT)

buttonN2 = tk.Button(windowNew, text="Stop",font=(14),command=onClickStop)
buttonN2.pack(padx=5, pady=25,side=tk.LEFT)


windowNew.mainloop()
