#!/usr/bin/python3
"""
This script adds all its arguments to a Python list
and then saves them to a file using the provided functions
save_to_json_file and load_from_json_file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Add command-line arguments to a Python list
    and save them to a file.
    If the file 'add_item.json' exists,
    load its contents into a list.
    If the file doesn't exist, initialize an empty list.
    Append command-line arguments to the list.
    Save the updated list to the file 'add_item.json' using JSON serialization.

    Parameters: none

    Returns: none
    """
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")


if __name__ == '__main__':
    main()
