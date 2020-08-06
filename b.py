#Q2
from tkinter import *
i=0
root=Tk()
l=Label(root,text="hi")
def fn():
    global i
    c=["red","blue","green","pink"]
    l.config(fg=c[i%4])
    i+=1
btn=Button(root,text="Click me",command=fn)
l.pack()
btn.pack()
root.mainloop()
