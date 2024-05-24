#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
    except IndexError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
