#!/usr/bin/python3
import sys
if __name__ == '__main__':
    result = 0
    if len(sys.argv) > 1:
        for number in sys.argv[1:]:
            result += int(number)
        print("{}".format(result))
    else:
        print(0)
