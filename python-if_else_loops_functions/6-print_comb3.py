#!/usr/bin/python3
for number1 in range(0,9):
    for number2 in range(1,10):
        if number1 == 8 and number2 ==9:
            print("{}{}".format(number1, number2))
        else:
            if number1 != number2 and number1 < number2:
                print("{}{}, ".format(number1, number2), end = "")
        
