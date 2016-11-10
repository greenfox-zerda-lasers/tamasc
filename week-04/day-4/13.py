from tkinter import *

master = Tk()

canvas = Canvas(width=600, height=600, bg='yellow')
canvas.pack()

def draw(n, size=400, x=0, y=0):
    colors = ['black', 'yellow', 'purple', 'blue', 'red']
    color1 = colors[n%len(colors)-1]
    color2 = colors[(n-1)%len(colors)-2]
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

draw(4, 600)
master.mainloop()
