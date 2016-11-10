from tkinter import *

master = Tk()

canvas = Canvas(width=1000, height=1000, bg='yellow')
canvas.pack()

def draw(size, n, x0=0, y0=0):
    if n == 0 or size < 3:
        return
    else:
        canvas.create_line(x0+size/3,y0+0,x0+size/3,y0+size)
        canvas.create_line(x0+size*2/3,y0+0,x0+size*2/3,y0+size)
        canvas.create_line(x0+0,y0+size/3,x0+size,y0+size/3)
        canvas.create_line(x0+0,y0+size*2/3,x0+size,y0+size*2/3)
        n = n-1
        draw(size/3, n, x0+size/3, y0)
        draw(size/3, n, x0, y0+size/3)
        draw(size/3, n, x0+size*2/3, y0+size/3)
        draw(size/3, n, x0+size*1/3, y0+size*2/3)

draw(860, 8)

master.mainloop()
