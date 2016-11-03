numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)


# 1st version
# def minim(numbers):
#     minnum=numbers[0]
#     for x in numbers:
#         if minnum > x:
#             minnum = x
#     return minnum

# 2nd (better) version
def minim(numbers):
    minnum=numbers[0]
    for x in range(1, len(numbers)):
        if minnum > numbers[x]:
            minnum = numbers[x]
    return minnum


print(minim(numbers))
