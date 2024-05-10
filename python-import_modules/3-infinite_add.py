#!/usr/bin/python3
import sys
if __name__ == '__main__':
    result = 0
    if len(sys.argv) > 1:
        for number in sys.argv:
            result += int(number)
        print("{}".format(result))
