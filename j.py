import turtle
t=turtle.Turtle()
x=100
for i in range(25):
    t.forward(x)
    t.right(90)
    x-=4
x+=4
t.right(90)
for i in range(25):
    t.forward(x)
    t.right(90)
    x+=4
