#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = str(abs(value))
        if x.isdigit():
            print("{:d}".format(value))
            return True
    except TypeError:
        return False
    finally:
        pass
