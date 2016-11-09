# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300


def checkerboard(a):                           #takes 1 parameter: size of a checkerboard pattern's square's side
    for j in range(0, 9, 1):
        for i in range(0, 9, 2):
            canvas.create_rectangle(0+i*a+j%2*a, 0+j*a, a+i*a+j%2*a, a+j*a, fill = 'black')

canvas = Canvas(width=cv_width, height=cv_height, bg='white')
canvas.pack()

checkerboard(38)


master.mainloop()
