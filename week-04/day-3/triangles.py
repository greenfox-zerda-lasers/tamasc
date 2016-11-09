from tkinter import *
import math

master = Tk()

canvas_size = 500

def line(x0, y0, x1, y1):
    canvas.create_line(x0, y0, x1, y1, fill='green')

canvas = Canvas(width=canvas_size*1.3, height=canvas_size)
canvas.pack()

def triangles(num, side, x0, y0): #num=max number of triangles in a row, side=the length of the main triangle(length), x0,y0=top corner position of the main traingle
    x = int(side/num)
    for i in range(0, side+2, x):
        line(x0-side/2+side/2-i*1/2, y0+0+i*math.sqrt(3)/2, x0-side/2+side/2+i*1/2, y0+0+i*math.sqrt(3)/2)
        line(x0-side/2+0+i, y0+side*math.sqrt(3)/2, x0-side/2+side/2+i/2, y0+0+i*math.sqrt(3)/2)
        line(x0-side/2+side/2-i/2, y0+0+i*math.sqrt(3)/2, x0-side/2+side-i, y0+side*math.sqrt(3)/2)


triangles(120, 500,250,00)


master.mainloop()
