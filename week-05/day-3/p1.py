# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_numbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('fail')
