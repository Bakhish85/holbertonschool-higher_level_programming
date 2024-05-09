#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for index, element in enumerate(sys.argv[1:]):
            print("{}: {}".format(index, element))
