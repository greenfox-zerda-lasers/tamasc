from tkinter import *

master = Tk()

canvas = Canvas(width=600, height=600, bg='yellow')
canvas.pack()

def draw_square(x,y, size):
    canvas.create_rectangle(x, y, x+size, y+size, fill='green', outline='yellow')

def draw(n, size, x=0, y=0):
    if n == 0 or size < 3:
        return
    else:
        draw_square(x, y, size)
        n = n - 1
        draw(n, size/3, x, y)
        draw(n, size/3, x+size/1.5, y+size/1.5)
        draw(n, size/3, x+size/1.5, y)
        draw(n, size/3, x, y+size/1.5)


draw(10, 600)
master.mainloop()
