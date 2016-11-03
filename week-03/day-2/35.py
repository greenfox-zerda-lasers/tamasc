# create a function that returns it's input factorial

def faktorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

print(faktorial(5))
