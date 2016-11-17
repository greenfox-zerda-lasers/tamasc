# Create a "robot" class that manifests a robots's memory
# make sure that you implement the following things:
#  - the robot can remember new things (simple string)
#  - the robot can recall things (as strings)
#  - the robot has a name
#  - the robot has list of possible mood
#  - the robot has a position property
#  - the robot can move by calling a method that sets its position

from random import randint
import datetime

class Robot_model():

    def __init__(self, name):
        self.mood_list = ['happy', 'angry', 'sad', 'hungry', 'thirsty', 'horny', 'calm', 'confused', 'crazy', 'excited']
        self.name = name
        self.position = [randint(0,100), randint(0,100)]
        self.memory = ['I was born in ' + str(datetime.datetime.now())]
        self.mood = self.mood_list[randint(0,len(self.mood_list)-1)]
