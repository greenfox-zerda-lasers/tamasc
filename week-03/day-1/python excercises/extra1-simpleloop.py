h = 5

x='*'
n=1
m=0


for i in range(h*2-1):
    m+=1*n
    print(x * m)
    if m == h:
        n=n*-1
