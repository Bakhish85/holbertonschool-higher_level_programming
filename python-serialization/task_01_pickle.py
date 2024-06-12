#!/usr/bin/env python3
"""
This module provides a simple mechanism for serializing
and deserializing Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """
    A custom Python class representing a simple
    object with attributes like name, age, and student status.

    Methods:
        - __init__(self, name, age, is_student): Initializes
                    a new CustomObject instance
                    with the given attributes.
        - display(self): Displays the attributes of the object.
        - serialize(self, filename): Serializes the object
                    to a binary file using the pickle module.
        - deserialize(cls, filename): Deserializes a CustomObject
                    instance from a binary file.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
            pass

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                new_obj = pickle.load(f)
                return new_obj
            pass
        except FileNotFoundError:
            return None
        except IOError:
            return None
