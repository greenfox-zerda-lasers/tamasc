# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():
    grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

jancsi = Student()

jancsi.add_grade(3)
jancsi.add_grade(1)
jancsi.add_grade(5)
jancsi.add_grade(1)
jancsi.add_grade(3)
jancsi.add_grade(4)
print(jancsi.grades)
print(jancsi.get_average())
