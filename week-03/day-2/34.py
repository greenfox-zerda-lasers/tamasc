numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def ownsum(array):
    num = 0
    for x in array:
        num += x
    return num
print(ownsum(numbers))
