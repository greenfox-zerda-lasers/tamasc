import sys, getopt
from todo_view import Todo_view
from todo_model import Todo_model


class Todo():

    def __init__(self, list_name):
        self.model = Todo_model(list_name)
        self.view = Todo_view()

        self.get_args(sys.argv[1:])

    def complete_task(self, task):
        self.model.complete_task(task)
        self.model.update_file()

    def remove_task(self, task):
        self.model.remove_task(task)
        self.model.update_file()

    def add_task(self, task):
        self.model.add_task(task)
        self.model.update_file()

    def list_tasks(self):
        self.model.list()

    def usage(self):
        self.view.usage()

    def get_args(self,argv):
        try:
            opts, args = getopt.getopt(argv,"la:r:c:")
        except getopt.GetoptError:
            sys.exit(2)

        if len(opts) == 0:
            self.usage()

        for opt, arg in opts:
            if opt == '-l':
                self.list_tasks()
            elif opt in ("-a"):
                self.add_task(arg)
            elif opt in ("-r"):
                self.remove_task(arg)
            elif opt in ("-c"):
                self.complete_task(arg)

x = Todo('my_list')
