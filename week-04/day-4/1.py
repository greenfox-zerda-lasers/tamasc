# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def final_countdown(number):
    if number <= 1:  #bascase
        print(number)
    else:
        print(number)
        return final_countdown(number-1)

final_countdown(995)
