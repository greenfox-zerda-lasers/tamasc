# create a function that takes a list and returns a new list with all the elements doubled

def double(list):
    double_list = []
    for element in list:
        double_list.append(element * 2)
    return double_list

print(double([1,2,3,4]))
