from tkinter import *
import time
import random

master = Tk()

canvas = Canvas(width=600, height=600, bg='white')
canvas.pack()

m_ratio = 3**.5/2

def random_color():
    return '#' + str(random.randint(0,9))+ str(random.randint(0,9))+ str(random.randint(0,9))

def draw_hexagon(x, y, size, x0=150, y0=0):
    color1 = random_color()
    color2 = random_color()
    canvas.create_polygon(x0 + x, y0 + y, x0 + x + size, y0 + y, x0 + x + size*3/2, y0 + y + size*m_ratio,
                         x0 + x + size, y0 + y + size*2*m_ratio, x0 + x, y0 + y + size*2*m_ratio,
                         x0 + x - size/2, y0 + y + size*m_ratio,
                         fill=color1, outline=color2)

def draw(n, size, x=0, y=0):
    time.sleep(0.0000000000001)
    canvas.update()
    if n == 0 or size < 3:
        return
    else:
        draw_hexagon(x, y, size)
        n = n - 1
        draw(n, size/3, x, y)
        draw(n, size/3, x+size*2/3, y)
        draw(n, size/3, x-size/3, y+size*m_ratio*2/3)
        draw(n, size/3, x+size, y+size*m_ratio*2/3)
        draw(n, size/3, x, y+size*m_ratio*4/3)
        draw(n, size/3, x+size*2/3, y+size*m_ratio*4/3)


draw(4, 250, 0, 50)
# draw(5,300, 150, 150)
master.mainloop()
