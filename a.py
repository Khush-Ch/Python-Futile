#Q1
from tkinter import * 
root=Tk() 
label=Label(root) 
counter=0
i=0
def count():
    global i
    i=1
def ct(): 
    global counter 
    global i
    if i==0:
        counter+=1 
        label.config(text=str(counter)) 
        label.after(100,ct) 
ct() 
button=Button(root, text="STOP", command=count) 
button.grid(row=1, column=0) 
label.grid(row=0, column=0) 
 
