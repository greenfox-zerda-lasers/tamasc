# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def number_of_lines(file_name):
    try:
        fr = open(file_name, 'r')
    except FileNotFoundError:
        return 0
    line_number = 0
    for line in fr:
        line_number += 1
    fr.close()
    return line_number
