y = 'seasons'
out = 6
# if the last and the first letter of the string
# are the same double the variable
# called out, if not half it
if y[0] == y[-1]:
    out = out*2
else:
    out = out/2
print(out)
