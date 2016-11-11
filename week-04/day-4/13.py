from tkinter import *
import random
import time

master = Tk()

canvas = Canvas(width=600, height=600, bg='white')
canvas.pack()

def random_color():
    return '#' + str(random.randint(0,9))+ str(random.randint(0,9))+ str(random.randint(0,9))

def draw(n, size=400, x=0, y=0):
    time.sleep(0.0001)
    canvas.update()
    color1 = random_color()
    color2 = random_color()
    if n == 0 or size < 3:
        return
    else:
        canvas.create_polygon(x+size/4, y+0, x+size*3/4, y+0,
                                x+size, y+size/2, x+size*3/4, y+size,
                                x+size*1/4, y+size, x+0, y+size/2,
                                fill=color1, outline=color2)
        n = n - 1
        print(size/2, x+size/8)
        draw(n, size/2, x+size/8, y+0)
        draw(n, size/2, x+size*4/8, y+size*2/8)
        draw(n, size*4/8, x+size/8, y+size*4/8)

draw(5, 600)
master.mainloop()
