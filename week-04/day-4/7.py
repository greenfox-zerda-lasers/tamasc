# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(string):
    if len(string) == 0:
        return ''
    elif string[0] == 'x':
        return 'y' + x_to_y(string[1:])
    else:
        return string[0] + x_to_y(string[1:])

print(x_to_y('axxyxyyysxysyayxyayxysayxyasxyasyxysayxyasyxyas'))
