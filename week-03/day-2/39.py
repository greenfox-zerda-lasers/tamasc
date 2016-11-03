names = ['Zakarias', 'Hans', 'Otto', 'Ole', 'd', 'asdasdfsadfsdf']
# create a function that returns the shortest string
# from a list

def shortest_string(names):
    short_name=names[0]
    for name in names:
        if len(name) < len(short_name):
            short_name = name
    return short_name

print(shortest_string(names))
