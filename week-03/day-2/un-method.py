def union(list1, list2):
    uni=list1
    for x in list2:
        i = 0
        for y in uni:
            if x == y:
                i += 1
        if i == 0:
            uni.append(x)
    return uni


print(union([1,4,3, 45],[3,4,5, 56, 67, 45, 45, 45]))
