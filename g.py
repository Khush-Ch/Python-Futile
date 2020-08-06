#Q7
from tkinter import *
import tkinter.messagebox
from tkinter import Toplevel
root1=Tk()
tkinter.messagebox.showinfo("Fact","Life is all about up's and down's")

ans=tkinter.messagebox.askquestion("Q1","Do u like ice-cream??")
if ans=="yes":
    print("Crazy")
else:
    print("Okay!")

root2=Tk()
t=tkinter.Toplevel()
t.title("This is top level window")
t.focus_force()
