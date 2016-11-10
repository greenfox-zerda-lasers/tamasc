# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_to_y(string):
    if len(string) == 0:
        return ''
    elif string[0] == 'x':
        return x_to_y(string[1:])
    else:
        return string[0] + x_to_y(string[1:])

print(x_to_y('axxyxyyysxysyayxyayxysayxyasxyasyxysayxyasyxyas'))
