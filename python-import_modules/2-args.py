#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))
    else:
        if len(sys.argv) == 2:
            print("{} argument:".format(len(sys.argv)-1))
            for index, element in enumerate(sys.argv[1:]):
                print("{}: {}".format(index+1, element))
        else:
            print("{} arguments:".format(len(sys.argv)-1))
            for index, element in enumerate(sys.argv[1:]):
                print("{}: {}".format(index+1, element))
