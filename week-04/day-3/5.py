# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def line_fifty(x, y):
    canvas.create_line(x, y, x+50, y)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

line_fifty(12,12)
line_fifty(110,50)
line_fifty(222,200)


master.mainloop()
