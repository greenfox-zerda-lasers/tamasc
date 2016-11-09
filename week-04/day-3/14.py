# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.

from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def line(x0, y0, x1, y1, color):
    canvas.create_line(x0, y0, x1, y1, fill=color)

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

for i in range(0, cv_width, 20):
    line(0, i, i, cv_width, 'green')
    line(i, 0, cv_width, i, 'purple')


master.mainloop()
