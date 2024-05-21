#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    This function converts a Roman numeral to an integer.
    Args:
        roman_string (str): The input string - roman numeral.
    Returns:
        int:    Must return an integer. 
            - You can assume the number will be between 1 to 3999.
            - If the roman_string is not a string or None, return 0.
    """
    if type(roman_string) != str:
        return 0
    elif roman_string == None:
        return 0
    else:
        number = 0
        for i, symbol in enumerate(roman_string):
            if symbol == 'M':
                if roman_string[i-1] == 'C' and i != 0:
                    number += 800
                else:
                    number += 100
            elif symbol == 'D':
                if roman_string[i-1] == 'C' and i != 0:
                    number += 300
                else:
                    number += 500
            elif symbol == 'C':
                if roman_string[i-1] == 'X' and i != 0:
                    number += 89
                else:
                    number += 100
            elif symbol == 'L':
                if roman_string[i-1] == 'X' and i != 0:
                    number += 39
                else:
                    number += 50
            elif symbol == 'X':
                if roman_string[i-1] == 'I' and i != 0:
                    number += 8
                else:
                    number += 10
            elif symbol == 'V':
                if roman_string[i-1] == 'I' and i != 0:
                    number += 3
                else:
                    number += 5
            elif symbol == 'I':
                number += 1
        return number
