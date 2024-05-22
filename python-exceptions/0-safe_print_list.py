#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for number in my_list:
            if count < x:
                count += 1
                print("{}".format(number), end="")
        print("")
    except:
        print("Unknown error")
    finally:
        return count
