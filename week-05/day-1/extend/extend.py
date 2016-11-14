
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    return max(a, b, c)

# Returns the median value of a list given as param
def median(pool):
    if isinstance(pool, str) or isinstance(pool, bool):
        raise TypeError("input parameter must be a list of ints of floats, or an int")
    pool = sorted(pool)
    x = (len(pool) - 1)/2
    return (pool[int(x)] + pool[int(x + 0.5)])/2

# Returns true if the param is a vovel
def is_vovel(char):
    if not isinstance(char, str):
        raise TypeError("Don't be silly, input parameter must be a string")
    return char.lower() in 'aeiouéáőűöüúóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    if not isinstance(hungarian, str):
        raise TypeError("Don't be silly, input parameter must be a string")
    teve = ''
    for char in hungarian:
        if is_vovel(char):
            teve = teve + char + 'v' + char
        else:
            teve = teve + char
    return teve
