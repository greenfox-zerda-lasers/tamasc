import sys, getopt
import proba

class Todo:

    def __init__(self, list_name):
        self.list_name = list_name

    def complete_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def add_task(self, task):
        pass

    def list_tasks(self):
        pass

    def get_args(self,argv):
        try:
            opts, args = getopt.getopt(argv,"la:r:c:")
            print(opts)
        except getopt.GetoptError:
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-l':
                self.list_tasks()
            elif opt in ("-a"):
                self.add_task(arg)
            elif opt in ("-r"):
                self.remove_task(arg)
            elif opt in ("-c"):
                self.complete_task(arg)
