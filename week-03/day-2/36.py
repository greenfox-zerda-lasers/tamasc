numbers = [3, 4, 5, 6, 7, 'kokusz', 'dio']
# write a function that reverses a list
def rev(numbers):
    revnumbers = []
    for i in range (len(numbers)-1, -1, -1):
        revnumbers.append(numbers[i])
    return revnumbers

print(rev(numbers))
