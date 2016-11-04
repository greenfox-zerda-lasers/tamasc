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


def pine(lines):
    chars = int(lines * 2 + 1)
    stars = 1
    spaces =  int((chars - stars) / 2)
    i = 0
    while i < lines:
        print(' '*spaces + '*'*stars)
        i += 1
        stars += 2
        spaces = int((chars - stars) / 2)
    while i > -1:
        print(' '*spaces + '*'*stars)
        i -= 1
        stars -= 2
        spaces = int((chars - stars) / 2)



pine(12)
