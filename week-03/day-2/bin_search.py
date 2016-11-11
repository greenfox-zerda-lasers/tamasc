
###### Test if sorted ###########
def sort_test(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

###### Sorting #################
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

###### Search #################
def traverse(list, number):
    i = int(len(list)/2)
    if list[i] == number:
        return True                 #basecase 1
    elif len(list) < 1:
        return False                #basecase 2
    elif list[i] > number:
        list = list[:i]
        return traverse(list, number)    #  <---- have to return
    else:
        list = list[i+1:]
        return traverse(list, number)    #  <---- have to return

###### Main function ############
def binary_search(list, number):
    if sort_test(list) is False:
        list = bubble_sort(list)
    return traverse(list, number)


x = binary_search([3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 3, 4, 5, 56, 67, 45,
                   45, 45, 3, 5, 3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 1], 1)

print(x)
