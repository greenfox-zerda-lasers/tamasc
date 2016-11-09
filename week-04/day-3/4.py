# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def line_to_center(x, y):
    canvas.create_line(x, y, cv_width/2, cv_height/2)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

line_to_center(0,0)
line_to_center(110,50)
line_to_center(250,200)


master.mainloop()
