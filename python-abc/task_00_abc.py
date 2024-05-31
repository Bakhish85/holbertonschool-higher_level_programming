"""
Module: animal_sounds.py

This module defines classes representing animals and their sounds.

Classes:
        Animal: An abstract base class representing an animal.
        Dog: A class representing a dog, inheriting from Animal.
        Cat: A class representing a cat, inheriting from Animal.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal class represents an abstract base class for all animals.

    Methods:
        sound(): Abstract method representing the sound of the animal.
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class represents a dog, inheriting from Animal.

    Methods:
        sound(): Returns the sound of a dog.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class represents a cat, inheriting from Animal.

    Methods:
        sound(): Returns the sound of a cat.
    """
    def sound(self):
        return "Meow"
