# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

master = Tk()

canvas = Canvas(width=300, height=300, bg='black')
canvas.pack()

master.mainloop()
