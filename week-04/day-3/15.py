# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def polygon(list, color):
    canvas.create_polygon(list, fill = color)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

polygon_coords = [[[10, 10], [290,  10], [290, 290], [10, 290]], [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70]], [[120, 100], [85, 130], [50, 100]]]
colors = ['green', 'red', 'yellow']

for i in range(len(polygon_coords)):
    polygon(polygon_coords[i], colors[i%len(colors)])

master.mainloop()
