# Create a class the displays the Elevator art and navigation (list of commands)
import os
import time


class View_elevator:

    def __init__(self):
        pass

    def show_state(self, number_of_levels, position, number_of_people):
        os.system('clear')
        print("___________________________________")
        print("`._______level_______people_______.'")
        for i in range(number_of_levels, 0, -1):
            if i == position:
                print("   ||_||_[{}]_||_||__[{}]_||_|| ".format(' ' + str(position) + ' ', str(number_of_people).zfill(2)))
            else:
                print("   || ||       || ||       || ||   ")
        if position == 0:
            print('  _||_||_[{}]_||_||__[{}]_||_||_'.format(' ' + str(position) + ' ', str(number_of_people).zfill(2)))
        else:
            print('  _||_||_______||_||_______||_||_')
        print(".'_______________________________`.")

    def waiting(self, pre_level, post_level):
        for i in range(20):
            os.system('clear')
            time.sleep(0.0001)
            print('LEVEL {}'.format(pre_level) + ' '*i + '>>>>' + ' '*(30-i) + 'LEVEL {}'.format(post_level))
