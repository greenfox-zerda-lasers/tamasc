filename = 'alma.txt'
# create a function that reads a file and prints it's
# lines, also it should prepend an 'A' character
# to each line

def readfile(filename):
    path = 'E:\\tamasc\greenfox\\tamasc\week-03\day-2\\' + filename
    f = open(path, 'r')
    for line in f:
        print(line.rstrip() + 'A')
    f.close()

print(readfile(filename))
