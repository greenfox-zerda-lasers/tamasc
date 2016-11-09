# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

# star_coords = [[6.5,0], [9,5], [14,5.5], [10.5,9], [12,14], [6.5, 11.5], [2,14], [3.5,9], [0, 5.5], [5,5]]

from tkinter import *
import random

master = Tk()

cv_width = 300
cv_height = 300

canvas = Canvas(width=cv_width, height=cv_height, bg='black')
canvas.pack()


def star(x, y, color):
    canvas.create_polygon([6.5+x, 0+y], [9+x, 5+y], [14 + x, 5.5+y], [10.5+x, 9+y],
                          [12+x, 14+y], [6.5+x, 11.5+y], [2+x, 14+y], [3.5+x, 9+y], [0+x, 5.5+y],
                          [5+x, 5+y], fill = color)

def rand_stars(max_number_of_stars):
    for i in range(0, max_number_of_stars):
        color = '#' + str(random.randint(1,9))*3
        star(random.randint(0, 300), random.randint(0, 285), color)

rand_stars(455)


master.mainloop()
