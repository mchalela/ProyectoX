
"""Module with class definitions."""


class Person:
    """Class used to describe a Person. foo.

    Parameters
    ----------
    name: str
        Name of the Person. 
    age: positive int
        Age of the Person. Should be a positive integer.

    Attributes
    ----------
    birth: int
        Year of birth according to the Person's age.

    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.birth = 2020 - age

    def say_hello(self):
        """Say hello."""
        print(f"Hello! My name is {self.name} and I'm {self.age} years old.")