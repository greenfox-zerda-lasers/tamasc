# create a 300x300 canvas.
# draw its diagonals in green

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 200

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

canvas.create_line(0, 0, cv_width, cv_height)

master.mainloop()
