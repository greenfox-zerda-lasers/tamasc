# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def box(a):
    canvas.create_rectangle(cv_width/2 - a/2, cv_height/2 - a/2, cv_width/2 + a/2, cv_height/2 + a/2, fill = "green")

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

for i in range(0, 20):
    box(200 - i*10)


# box(10)
# box(34)
# box(60)
# box(234)


master.mainloop()
