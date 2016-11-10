from tkinter import *

master = Tk()

canvas = Canvas(width=600, height=600, bg='yellow')
canvas.pack()

def draw(n, size=400, x=0, y=0):
    colors = ['black', 'yellow', 'purple', 'blue', 'red']
    color1 = colors[n%len(colors)]
    color2 = colors[(n+3)%len(colors)]
    if n == 0:
        return
    else:
        canvas.create_polygon(20+x+size/4, 20+y+0, 20+x+size*3/4, 20+y+0,
                                20+x+size, 20+y+size/2, 20+x+size*3/4, 20+y+size,
                                20+x+size*1/4, 20+y+size, 20+x+0, 20+y+size/2, fill=color1, outline=color2)
        n = n - 1
        draw(n, size/2, x+size/8, y+0)
        draw(n, size/2, x+size*4/8, y+size/4)
        draw(n, size/2, x+size/8, y+size/2)

draw(8)
master.mainloop()
