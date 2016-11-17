# Create a robot controller class. This is the mind of the robot.
# It should take an user input by listening to user input:
# Default functionaly when the robot is switched on:
#  - Automatically names the robot
#  - Sets it's position
#
# List of commands:
#  1) memorize: add a new memory entry to the memory
#  2) recall: displays a list memories
#  3) move: increments the robot's position by one coordinate the N-S-E-W directions
#     - it also displays the new position
#  4) speak: it can introduce itself by saying its name and mood and last memory
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

from model_robot import Robot_model
from view_robot import View_robot

class Robot():

    def __init__(self, name):
        self.model = Robot_model(name)
        self.view = View_robot()
        print(self.view.messages('born').format(self.model.name, str(self.model.position[0]), str(self.model.position[1])))
        self.command_waiting()

    def memorize(self):
        print(self.view.messages('memo'))
        memory = input(self.view.messages('memo-input'))
        self.model.memory.append(memory)

    def recall(self):
        print(self.view.messages('recall'))
        for i, memo in enumerate(self.model.memory):
            print(str(i) + '. ' + memo + '\n')

    def move(self):
        print(self.view.messages('move'))
        moves = (input(self.view.messages('move-input'))).split(' ')
        self.model.position[0] += int(moves[0])
        self.model.position[1] += int(moves[1])
        print(self.view.messages('new_position').format(str(self.model.position[0]), str(self.model.position[1])))

    def speak(self):
        print(self.view.messages('speak').format(self.model.name, self.model.mood, self.model.memory[-1]))

    def command_waiting(self):
        while True:
            command = input('\nWaiting for commands:\n')
            if command == 'memorize':
                self.memorize()
            elif command == 'recall':
                self.recall()
            elif command == 'move':
                self.move()
            elif command == 'speak':
                self.speak()
            else:
                self.view.listing_commands()

robot = Robot('Laci')
