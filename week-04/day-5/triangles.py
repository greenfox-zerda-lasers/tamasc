from tkinter import *
import time

master = Tk()

canvas = Canvas(width=600, height=600, bg='white')
canvas.pack()

m_ratio = 3**.5/2

def draw_rectangle(x, y, size, x0=0, y0=0):
    canvas.create_polygon(x0 + x, y0 + y, x0 + x + size, y0 + y, x0 + x + size/2, y0 + y + size*m_ratio, fill='green', outline='white')

def draw(n, size, x=0, y=0):
    time.sleep(0.0000002)
    canvas.update()
    if n == 0 or size < 3:
        return
    else:
        draw_rectangle(x, y, size)
        n = n - 1
        draw(n, size/2, x, y)
        draw(n, size/2, x+size/2, y)
        draw(n, size/2, x+size/4, y+size*m_ratio/2)



draw(5,300, 150, 150)
master.mainloop()
