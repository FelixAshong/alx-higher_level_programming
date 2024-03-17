#!/usr/bin/python3
"""Rectangle class to represent a square"""


class Rectangle():
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of rectangle
        Return:
        width of rectangle."""
        return self.__width

    @property
    def height(self):
        """ height of rectangle
        Return:
        height of rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter of the width
        Arguments:
        value: value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter of the width
        Arguments:
        value: value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
