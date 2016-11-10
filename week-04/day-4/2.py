# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def addition(n):
    if n == 1:
        return n
    else:
        return n+addition(n-1)

print(addition(998))
