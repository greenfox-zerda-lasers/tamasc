import sys, getopt




def get_args(argv):
    try:
        opts, args = getopt.getopt(argv,"la:r:c:")
        print(opts)
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-l':
            # self.list_tasks()
            print('mukodik')
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            print('i')
        elif opt in ("-o", "--ofile"):
            # outputfile = arg
            pass

if __name__ == "__main__":
    get_args(sys.argv[1:])
