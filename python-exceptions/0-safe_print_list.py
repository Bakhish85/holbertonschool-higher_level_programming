#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for number in my_list:
            count += 1
            if count <= x:
                print("{}".format(number), end = "")
        print("")
    except:
        pass
    finally:
        if x <= len(my_list):
            return x
        else:
            return len(my_list) 
