# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

rainbow = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET']

def box(a, color):
    canvas.create_rectangle(cv_width/2 - a/2, cv_height/2 - a/2, cv_width/2 + a/2, cv_height/2 + a/2, fill = color)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

for i in range(0, 20):
    box(300 - i*15, rainbow[i%len(rainbow)])


# box(10)
# box(34)
# box(60)
# box(234)


master.mainloop()
