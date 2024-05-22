#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = str(abs(value))
        if x.isdigit():
            print(value)
            return True
    except TypeError:
        return False
    finally:
        pass
