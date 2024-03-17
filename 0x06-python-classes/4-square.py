#!/usr/bin/python3
"""square class main"""


class Square():
    """square class"""
    def __init__(self, size=0):
        """ Instance of class Square
    Arguments:

        @size: size of side of square"""

        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ area of square
        Return:
                area of square."""
        return self.__size ** 2

    @property
    def size(self):
        """ getter of size

    Return:
            value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of the size

    Arguments:

        value: value of size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
