# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def box(x, y, width, height, color):
    canvas.create_rectangle(x, y, x+width, y+height, fill = color)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

box(10,10, 30,45, 'green')
box(34, 211, 6, 78, '')
box(34,10, 30,45, 'purple')
box(234,254, 21, 45, 'yellow')


master.mainloop()
