#!/usr/bin/python3
"""
xml_serializer

Description: This module provides functions to serialize Python
dictionaries to XML format and deserialize XML files to Python
dictionaries.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This function Serializes a Python dictionary to XML
    format and saves it to the specified filename.

    Parameters:
        dictionary (dict): The Python dictionary to be serialized.
        filename (str): The filename where the XML data will be saved.

    Returns: None

    Exceptions: None
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    This function deserializes XML data from the specified
    filename and returns it as a Python dictionary.

    Parameters:
        filename (str): The filename from which XML data will be deserialized.

    Returns:
        data (dict): The deserialized Python dictionary.

    Exceptions:
        ValueError: Raised during type conversion if the XML data cannot
        be converted to the appropriate Python data type (e.g., int or float).
    """
    root = ET.parse(filename).getroot()
    data = {}
    for element in root:
        try:
            data[element.tag] = int(element.text)
        except ValueError:
            try:
                data[element.tag] = float(element.text)
            except ValueError:
                data[element.tag] = element.text
    return data
