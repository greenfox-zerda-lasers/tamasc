import sys, getopt


class Todo:

    def __init__(self, list_name):
        self.list_name = list_name
        pass

    def complete_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def add_task(self, task):
        pass

    def list_tasks(self):
        pass

    def get_args(self):
        try:
            opts, args = getopt.getopt(argv,"la:r:c:")
            print(opts)
        except getopt.GetoptError:
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-l':
                self.list_tasks()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
