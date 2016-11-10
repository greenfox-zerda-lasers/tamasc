# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power(base, n):
    if n == 0 and base == 0:              #basecase1
        return 'Collapse of the Universe'
    elif n == 0:                          #basecase2
        return 1
    elif n == 1:                          #basecase3
        return base
    else:
        return base*power(base,n-1)

print(power(0,0))
