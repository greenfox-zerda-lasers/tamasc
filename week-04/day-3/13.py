# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def line(x, y):
    canvas.create_line(x, y, cv_width/2, cv_height/2)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

for i in range(0, cv_width, 20):
    line(0, i)
    line(cv_width , i)
    line(i, 0)
    line(i, cv_width )

# box(10)
# box(34)
# box(60)
# box(234)


master.mainloop()
