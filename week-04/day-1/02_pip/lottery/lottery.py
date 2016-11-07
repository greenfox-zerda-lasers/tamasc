# Create a method that returns the five most frequent lottery number in a pretty table format
from prettytable import PrettyTable

def numbers_to_list():
    fr = open('otos.csv','r')
    all_numbers = []
    for line in fr:
        z = line[:-1]
        z = z.split(';')[-1:-6:-1]
        for i in z:
            all_numbers.append(i)
    fr.close()
    return all_numbers

def occurance_of_numbers():
    all_numbers = numbers_to_list()
    occurance = []
    for i in range(1,10):
        occurance.append(all_numbers.count(str(i)))
    return occurance

def sort_occurance():
    occurance = occurance_of_numbers()
    sorted_occurance = []
    for number, frequency in enumerate(occurance):
        sorted_occurance.append([number + 1, frequency])
    for i in range(len(sorted_occurance)):
        for j in range(len(sorted_occurance)-1):
            if sorted_occurance[j][1] > sorted_occurance[j+1][1]:
                temp = sorted_occurance[j]
                sorted_occurance[j] = sorted_occurance[j+1]
                sorted_occurance[j+1] = temp
    return sorted_occurance[-1:-6:-1]

def five_most_frequent():
    sorted_occurance = sort_occurance()
    x = PrettyTable()
    x.field_names = ["number", "frequency"]
    for i in sorted_occurance:
        x.add_row(i)
    y = print(x)
    return y
