# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def green_box(x, y):
    canvas.create_rectangle(cv_width/2 - x/2, cv_height/2 - y/2, cv_width/2 + x/2, cv_height/2 + y/2, fill = 'green')

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

green_box(10,10)


master.mainloop()
