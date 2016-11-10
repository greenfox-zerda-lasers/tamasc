# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separate(string):
    if len(string) == 0:                #basecase1
        return ''
    elif len(string) == 1:              #basecase2
        return string[0]
    else:
        return string[0] + '*' +separate(string[1:])

print(separate('fsdafasdfasgsdgasd'))
