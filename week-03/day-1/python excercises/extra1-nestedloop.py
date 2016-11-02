# initial variable
h = 10

# auxiliary variables
x = ''
n = 1
m = 0

# inception loop
for i in range(h*2-1):
    m+=1*n
    for j in range(1,m+1):
        x=x+'*'
    print(x)
    x=''
    if m == h:
        n=n*-1
