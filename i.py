#Q9
from tkinter import *
root=Tk()
c=Canvas(root)
c.pack()

points=[0,0,50,50,0,50]
c.create_polygon(points,outline="black",fill="blue")
c.create_rectangle(50,50,100,110,outline="black",fill="green")
c.create_oval(110,110,130,130,outline="black",fill="red")
c.create_line(130,130,170,170,fill="maroon")
c.create_arc(170,170,220,250,start=0,extent=90,outline="black",fill="violet")
root.mainloop()
