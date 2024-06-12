#!/usr/bin/env python3
"""
csv_to_json_converter Module

Description:    This module provides a function to
                convert CSV files to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    This function Converts a CSV file to JSON format.

    Parameters:

        - csv_file(str):    The path to the CSV file to be converted

    Returns:

        - True:     if the conversion was successful.
        - False:    if an exception occurred (e.g., file not found).

    Exceptions Handled:

        - FileNotFoundError: Raised when the specified CSV file is not found.
    """
    try:
        data = []
        with open(csv_file, encoding="utf-8") as csvf:
            csvreader = csv.DictReader(csvf)
            for rows in csvreader:
                data.append(rows)
        with open("data.json", "w", encoding="utf-8") as jsonf:
            json_string = json.dumps(data)
            jsonf.write(json_string)
        return True
    except FileNotFoundError:
        return False
