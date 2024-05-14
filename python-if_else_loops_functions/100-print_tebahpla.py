#!/usr/bin/python3
string = ""
char_list = []
for ascii_number in range(97,123):
    if ascii_number % 2 == 1:
        ascii_number -= 32
    string += chr(ascii_number)
char_list.extend(string)
char_list.reverse()
new_string = "".join(char_list)
print("{}".format(new_string), end="")
