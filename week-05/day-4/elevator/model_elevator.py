# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Model_elevator:

    def __init__(self, number_of_levels):
        self.number_of_levels = number_of_levels
        self.elevator_is_on = True
        self.people_in_elevator = 0
        self.position = 0

    def remove_people(self, removed_people):
        self.people_in_elevator -= removed_people
        if self.people_in_elevator < 0:
            self.people_in_elevator = 0

    def add_people(self, added_people):
        self.people_in_elevator += added_people

    def move_elevator(self, moving):
        if moving == 'u' and self.position != self.number_of_levels:
            self.position += 1
        elif moving == 'd' and self.position != 0:
            self.position -= 1
        else:
            return
