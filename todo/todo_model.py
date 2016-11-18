from csv import reader
from datetime import datetime

class Todo_model():

    def __init__(self, list_name):
        self.list_name = list_name
        self.check_file()
        self.todo_list = self.create_list_tasks()

# **********************System*********************************
    def check_file(self):
        try:
            fr = open(self.list_name + '.csv', 'r')
            fr.close()
            print('\nfile loaded:' + self.list_name + '.csv\n')
        except FileNotFoundError:
            fw = open(self.list_name + '.csv', 'w')
            fw.close()
            print('\nnew file created:' + self.list_name + '.csv\n')

    def create_list_tasks(self):
        list = []
        fr = open(self.list_name + '.csv', 'r')
        for lines in fr:
            list.append(lines.split('|'))
        fr.close()
        return list

    def update_file(self):
        fw = open(self.list_name + '.csv', 'w')
        for item in self.todo_list:
            fw.write(item[0] + '|' + item[1] + '|' + item[2])
        fw.close()
        print('\nFile updated: ' + self.list_name + '.csv\n')

# **********************Functionality********************************
    def list(self):
        for i, task in enumerate(self.todo_list):
            if task[1] == 'completed':
                print(str(i+1) + '. [x]' + task[2].rstrip())
            else:
                print(str(i+1) + '. [ ]' + task[2].rstrip())

    def add_task(self, task):
        task = [str(datetime.now()), 'doing', task + '\n']
        self.todo_list.append(task)
        self.update_file()

    def remove_task(self, task):
        del self.todo_list[int(task)-1]
        self.update_file()

    def complete_task(self, task):
        self.todo_list[int(task)-1][1] = 'completed'
        self.update_file()


# x = Todo_model("my_list")
# print(x.todo_list)
# x.add_task('fdsgdfgsdfg1')
# x.add_task('fdsgdfgsdfg2')
# x.list()
