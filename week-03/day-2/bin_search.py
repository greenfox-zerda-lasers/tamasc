def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return(list)


def sort_test(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


def binary_search(list, number):
    if sort_test(list) == False:
        list = bubble_sort(list)
    i = int(len(list)/2)
    if list[i] == number:
        print(True)
        return
    elif len(list) < 3:
        print(False)
        return
    elif list[i] > number:
        list = list[:i]
        binary_search(list, number)
    elif list[i] < number:
        list = list[i:]
        binary_search(list, number)

binary_search([3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 3, 4, 5, 56, 67, 45, 45, 45, 3, 5], 41)
