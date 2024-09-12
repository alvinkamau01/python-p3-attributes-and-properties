#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="default"):
        self._name = name  # Directly assign name; no need to call __str__()

    def get_name(self):
        return self._name

    def set_name(self, value):
        if len(value) < 1 or len(value) > 25:
            print("Name must be a string between 1 and 25 characters.")
        elif value not in APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
        else:
            self._name = value  # Only set _name if all checks pass
    
    name = property(get_name, set_name)

dog = Dog()