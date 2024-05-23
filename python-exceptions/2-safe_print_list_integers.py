#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for number in my_list:
        try:
            print("{:d}".format(number))
            count += 1
            if count == x:
                break
        except:
            continue
    print()
    return count
