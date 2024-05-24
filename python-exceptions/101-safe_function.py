#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except ZeroDivisionError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
    except Index Error as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
