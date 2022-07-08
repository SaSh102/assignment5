import turtle
import time
import math

pi= math.pi
win = turtle.Screen()
pen = turtle.Pen()
x = -10
size = 60

for i in range(1, 50):
    for j in range(i+2):
        pen.forward(size)
        pen.left(float(360/(i+2)))
        height= float(100/2*math.ten(pi/ i+2))
    pen.penup()
    pen.setpos(i, x)
    pen.goto(i-10, x)
    pen.pendown()
    x -= 15
    size += 15
win.mainloop()

time.sleep(15)