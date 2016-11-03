numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def even(numbers):
    for x in numbers:
        if x % 2 == 1:
            numbers.remove(x)
    return numbers



print(even(numbers))
