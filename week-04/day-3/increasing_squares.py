from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def diagonal_square(xy, a):  # i = represents the squares position on a diagonal line; a = size of the square
    canvas.create_rectangle(10+xy, 10+xy, 10+a+xy, 10+a+xy, fill = "purple")

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

def diagonal_squares(init_square_size, num_of_boxes):
    xy = 0
    square_size = 0
    for i in range(0, num_of_boxes):
        xy += square_size
        square_size = init_square_size+10*i
        diagonal_square(xy, square_size)

diagonal_squares(10,6)

master.mainloop()
