#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            number = 'FizzBuzz'
            print("{} ".format(number), end="")
        elif number % 3 == 0:
            number = 'Fizz'
            print("{} ".format(number), end="")
        elif number % 5 == 0:
            number = 'Buzz'
            print("{} ".format(number), end="")
        else:
            print("{} ".format(number), end="")
