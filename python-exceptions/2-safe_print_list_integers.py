#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for number in my_list:
        try:
            if count == x:
                break
            print("{:d}".format(number), end="")
            count += 1
        except ValueError:
            continue
    print()
    return count
