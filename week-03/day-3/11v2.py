# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def pine(lines, direction=1, initial_space=0):
    start = 0
    end = lines
    if direction == -1:
        start = lines - 1
        end = -1
    for i in range(start, end, 1 * direction):
        print(' ' * initial_space + ' ' * (lines - i) + '*' * (1 + 2* i))

def diamond(lines):
    lines = int(lines / 2 + 1)
    pine(lines)
    pine(lines-1, -1, 1)

diamond(8)
