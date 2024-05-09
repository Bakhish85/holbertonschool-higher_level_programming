#!/usr/bin/python3
result = ""
for number in range(0, 100):
    if number != 99:
        if number >= 0 and number <= 9:
            result += "0{}, ".format(number)
        else:
            result += "{}, ".format(number)
    else:
        result += "{}".format(number)
print(result)
