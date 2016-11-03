filename = 'alma.txt'
# write a function that reads a file and prints how many
# lines and characters in it

def readfile(filename):
    path = 'E:\\tamasc\greenfox\\tamasc\week-03\day-2\\' + filename
    lines = 0
    chars = 0
    f = open(path, 'r')
    for line in f:
        chars += len(line)
        lines += 1
    f.close()
    return lines, chars

print(readfile(filename))
