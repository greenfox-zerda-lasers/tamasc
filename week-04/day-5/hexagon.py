from tkinter import *
import random

master = Tk()

canvas = Canvas(width=600, height=600, bg='white')
canvas.pack()

m_ratio = 3**.5/2

def random_color():
    return '#' + str(random.randint(0, 9)) + str(random.randint(0, 9))+ str(random.randint(0, 9))

def draw_hexagon(x, y, size, n):
    color_range = ['black', 'white', 'blue', 'orange']
    color1 = color_range[(n+2)%len(color_range)]
    color2 = color_range[(n+1)%len(color_range)]
    print(color2)
    canvas.create_polygon(x, y, x + size, y, x + size*3/2, y + size*m_ratio,
                          x + size, y + size*2*m_ratio, x, y + size*2*m_ratio,
                          x - size/2, y + size*m_ratio,
                          fill=color1, outline=color2)

def draw(n, size, x=0, y=0):
    if n == 0 or size < 3:
        return
    else:
        draw_hexagon(x, y, size, n)
        n = n - 1
        draw(n, size/3, x, y)
        draw(n, size/3, x+size*2/3, y)
        draw(n, size/3, x-size/3, y+size*m_ratio*2/3)
        draw(n, size/3, x+size, y+size*m_ratio*2/3)
        draw(n, size/3, x, y+size*m_ratio*4/3)
        draw(n, size/3, x+size*2/3, y+size*m_ratio*4/3)


draw(5, 250, 175, 50)

master.mainloop()
