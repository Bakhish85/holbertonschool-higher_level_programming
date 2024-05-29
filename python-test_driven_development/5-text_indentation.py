#!/usr/bin/python3
"""
Module: text_indentation

This module provides a function for formatting text
with indentation based on specific punctuation marks.

Functions:
    - text_indentation(text):   Formats the given text
    with indentation based on specific punctuation marks.
"""


def text_indentation(text):
    """
    Formats the given text with indentation based on specific
    punctuation marks.

    Parameters:
        text(str):  The text to be formatted

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    mark_list = ['.', '?', ':']
    new_text = ""
    idx = 0
    while idx < len(text):
        if idx > 0 and text[idx-1] in mark_list and text[idx] == ' ':
            idx += 1
            continue
        elif text[idx] in mark_list:
            new_text += text[idx]
            new_text += '\n\n'
            idx += 1
            continue
        new_text += text[idx]
        idx += 1
    print(new_text, end="")
