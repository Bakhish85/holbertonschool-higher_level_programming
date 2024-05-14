#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    new_list = []
    new_list.extend(str)
    for i, char in enumerate(new_list):
        if i != n:
            new_str += char
    return new_str
