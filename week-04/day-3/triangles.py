from tkinter import *
import math

master = Tk()

canvas_size = 500

def line(x0, y0, x1, y1):
    canvas.create_line(x0, y0, x1, y1, fill='green')

canvas = Canvas(width=canvas_size*1.3, height=canvas_size)
canvas.pack()

def triangles(num, side):
    x = int(side/num)
    print(x)
    for i in range(0, side, x):
        line(side/2-i*1/2, 0+i*math.sqrt(3)/2, side/2+i*1/2, 0+i*math.sqrt(3)/2)
        line(0, side/2, side/2+i/2, 0+i*math.sqrt(3)/2)


triangles(10, 300)


master.mainloop()
