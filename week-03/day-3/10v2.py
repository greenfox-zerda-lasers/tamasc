#       *        1 line 0 space
#      ***       2 line 1 space
#     *****      3 line 2 space
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def pine(lines):
    for i in range(0, lines):
        print(' ' * (lines - i) + '*' * (1 + 2* i))

pine(5)
