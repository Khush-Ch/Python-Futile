#Q3
from tkinter import *
i=0
l=[];n=[];b=[];e=[]
n.append(Tk())
l.append(Label(n[0],text=i+1).pack())
def fn():
    global i
    i+=1
    n.append(Tk())
    l.append(Label(n[i],text=i+1).pack())
    b.append(Button(n[i],text="Next",command=fn).pack())
    e.append(Button(n[i],text="Exit",command=n[i].destroy).pack())
    
b.append(Button(n[0],text="Next",command=fn).pack())
e.append(Button(n[0],text="Exit",command=n[0].destroy).pack())
