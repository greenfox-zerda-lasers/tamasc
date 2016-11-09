from tkinter import *

master = Tk()

cv_width = 300
cv_height = 300

def diagonal_square(i, a):  # i = represents the squares position on a diagonal line; a = size of the square
    canvas.create_rectangle(i*a, i*a, a+i*a, a+i*a, fill = "purple")

canvas = Canvas(width=cv_width, height=cv_height)
canvas.pack()

def diagonal_squares(num_of_boxes, square_size):
    for j in range(1, num_of_boxes+1):
        diagonal_square(j,square_size)

diagonal_squares(19,11)


master.mainloop()
