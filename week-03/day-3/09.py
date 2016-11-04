# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has


# v1
# def half_pine(number):
#     for i in range(1,number+1):
#         line = ''
#         for j in range(i):
#             line += '*'
#         print(line)

#  v2
def half_pine(number):
    for i in range(1,number+1):
        print('*' * i)

half_pine(5)
