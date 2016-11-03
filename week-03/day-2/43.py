filename = 'alma.txt'
# create a function that prints the content of the
# file given in the input

def readfile(filename):
    path = 'E:\\tamasc\greenfox\\tamasc\week-03\day-2\\' + filename
    f = open(path, 'r')
    for line in f:
        print(line)
    f.close()

print(readfile(filename))
