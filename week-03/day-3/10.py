# Create a function that prints a triangle like this:
#       *        1 line 0 space
#      ***       2 line 1 space
#     *****      3 line 2 space
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def pine(lines):
    chars = int(lines * 2 + 1)
    stars = 1
    spaces =  int((chars - stars) / 2)
    i = 0
    while i < lines:
        print(' '*spaces + '*' * stars)
        i += 1
        stars += 2
        spaces = int((chars - stars) / 2)



pine(20)
