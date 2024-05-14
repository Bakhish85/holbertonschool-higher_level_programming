#!/usr/bin/env python3
char_list = []
for ascii_number in range(97,123):
    if ascii_number % 2 == 1:
        ascii_number -= 32
    char_list.append(chr(ascii_number))
char_list.reverse()
print("".join(char_list), end="")
