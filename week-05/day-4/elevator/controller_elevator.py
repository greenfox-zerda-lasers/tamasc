# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

from model_elevator import Model_elevator
from view_elevator import View_elevator

class Elevator():

    def __init__(self, number_of_levels):
        self.model = Model_elevator(number_of_levels)
        self.view = View_elevator()
        self.loop()

    def elevator_onof(self):
        if self.model.elevator_is_on == True:
            self.model.elevator_is_on = False
            print('Elevator turned off')
        else:
            self.model.elevator_is_on = True
            print('Elevator turned on')

    def loop(self):
        while self.model.elevator_is_on:
            pre_level = self.model.position
            self.model.add_people(self.check_input(input('\nEntering people: ')))
            self.model.remove_people(self.check_input(input('\nLeaving people: ')))
            self.model.move_elevator(input('\nMove (u/d): '))
            self.view.waiting(pre_level, self.model.position)
            self.view.show_state(self.model.number_of_levels, self.model.position, self.model.people_in_elevator)

    def check_input(self, input_var):
        try:
            return int(input_var)
        except ValueError:
            print('number of people must be an positive integer')
            return 0

elevator = Elevator(10)
