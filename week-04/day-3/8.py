# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def box(x, y, color):
    canvas.create_rectangle(x, y, x + 50, y + 50, fill = color)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

box(10, 10, 'green')
box(34, 211, '')
box(60,60, 'purple')
box(234,254, 'yellow')


master.mainloop()
