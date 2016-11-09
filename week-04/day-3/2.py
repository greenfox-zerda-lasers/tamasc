from tkinter import *


master = Tk()

canvas = Canvas(width=300, height=300, bg='black')
canvas.pack()

line_coords = [[50, 50, 200, 50], [200, 50, 200, 100], [200, 100, 50, 100], [50, 100, 50, 50]]
line_colors = ['green', 'blue', 'yellow', 'white']

for i in range(0,4):
    canvas.create_line(line_coords[i], fill=line_colors[i])

master.mainloop()
