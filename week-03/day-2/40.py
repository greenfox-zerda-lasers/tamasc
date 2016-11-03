students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def sum_of_candies(students):
    candies = 0
    for x in students:
        if x['age'] < 10:
            candies += x['candies']
    return candies

print(sum_of_candies(students))
