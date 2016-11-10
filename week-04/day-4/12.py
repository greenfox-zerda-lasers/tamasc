# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

# V1
# def add_r(li):
#     if len(li) == 1 and not isinstance(li[0], list):
#         return li[0]
#     elif len(li) == 1 and isinstance(li[0], list):
#         return add_r(li[0])
#     elif isinstance(li[0], list):
#         return add_r(li[0]) + add_r(li[1:])
#     else:
#         return li[0] + add_r(li[1:])


# V2 better version
def add_r(li):
    if len(li) == 0:
        return 0
    elif isinstance(li[0], list):
        return add_r(li[0]) + add_r(li[1:])
    else:
        return li[0] + add_r(li[1:])

print(add_r([1, 2, [3, 4, 1,[2,3,4,[4,6,2], 4, [4]]]]))
