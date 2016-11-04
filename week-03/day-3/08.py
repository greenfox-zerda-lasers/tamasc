# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name = 'Istvan', last_name = 'Kovacs'):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.last_name + " " + self.first_name)

class Student(Person):
        grades = []

        def add_grade(self, grade):
            self.grades.append(grade)

        def get_average(self):
            return sum(self.grades) / len(self.grades)

        def greet(self):
            print(self.last_name + " " + self.first_name + " " + str(self.get_average()))

tomi = Student('Tamas', 'Czerjak')



tomi.add_grade(4)
tomi.add_grade(5)
tomi.greet()
