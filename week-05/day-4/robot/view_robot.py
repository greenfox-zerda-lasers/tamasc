# Create a class that displays the robot's messages, position, etc

class View_robot():

    def __init__(self):
        self.message_list = {'born':"My name is {} and I'm at N{} E{} position",
                             'memo':'Command memorize\n',
                             'memo-input':'What should I memorize?: ',
                             'recall':'Command recall\n',
                             'move-input':'Move to position \n(2 arguments separeted with spaces, corresponding to directions of N and E):',
                             'move':'Command move\n',
                             'new_position': 'My new position is N{} E{}.\n',
                             'speak':"Hello, my name is {}. I'm {} now. {}"}

    def messages(self, code):
        return str(self.message_list[code])

    def listing_commands(self):
        print('\n\n*******************')
        print('*List of commands:*')
        print('*-----------------*')
        print('*     speak       *')
        print('*      move       *')
        print('*    memorize     *')
        print('*     recall      *')
        print('*******************')

# x = View_robot()
# print(x.messages('born').format('dfsfsdf', '43', 'x.model.position[1]'))
