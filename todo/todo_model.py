class Todo_model():

    def __init__(self,list_name):
        self.list_name = list_name
        self.check_file()

    def check_file(self):
        try:
            fr = open(self.list_name + '.csv', 'r')
            fr.close()
            print('\nloading file:' + self.list_name + '.csv')
        except FileNotFoundError:
            fw = open(self.list_name + '.csv', 'w')
            fw.close()
            print('\ncreating new file:' + self.list_name + '.csv')
