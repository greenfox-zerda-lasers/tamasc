

from tkinter import *

master = Tk()

canvas_size = 300

def line(x0, y0, x1, y1):
    canvas.create_line(x0, y0, x1, y1, fill='green')

canvas = Canvas(width=canvas_size, height=canvas_size)
canvas.pack()


def nato(distance_of_lines):
    for i in range(0, int(canvas_size/2+1), distance_of_lines):
        line(0+i, canvas_size/2, canvas_size/2, canvas_size/2-i-distance_of_lines)
        line(canvas_size/2, 0+i-distance_of_lines, canvas_size/2+i, canvas_size/2)
        line(0+i, canvas_size/2, canvas_size/2, canvas_size/2+i+distance_of_lines)
        line(canvas_size/2, canvas_size/2+i+distance_of_lines, canvas_size-i, canvas_size/2)

nato(10)


master.mainloop()
