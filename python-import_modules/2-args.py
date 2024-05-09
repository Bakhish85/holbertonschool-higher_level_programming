#!/usr/bin/python3
import sys
if __name__ == '__main__'
    if len(sys.argv) == 0:
        print("{} arguments.".format(len(sys.argv)))
    else:
        print("{} arguments:".format(len(sys.argv)))
        for index, element in enumerate(sys.argv):
            print("{}: {}".format(index+1, element))
