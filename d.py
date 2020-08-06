#Q4
from tkinter import *
root=Tk()
a=["red","blue","green","yellow","maroon"]
def fn(i):
    l=Label(root,text=a[i],bg=a[i],width=60).grid(row=1,columnspan=5)            
b1=Button(root,text="red",command=lambda:fn(0),width=10).grid(row=0,column=0)
b2=Button(root,text="blue",command=lambda:fn(1),width=10).grid(row=0,column=1)
b3=Button(root,text="green",command=lambda:fn(2),width=10).grid(row=0,column=2)
b4=Button(root,text="yellow",command=lambda:fn(3),width=10).grid(row=0,column=3)
b5=Button(root,text="maroon",command=lambda:fn(4),width=10).grid(row=0,column=4)
