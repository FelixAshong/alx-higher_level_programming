#!/usr/bin/python3
"""contains classes to represent different shapes"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class to represent rectangles"""
    def __init__(self, width, height):
        """initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """evaluates the area"""
        return self.__width * self.__height

    def __str__(self):
        """formatted output"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square class to represent squares"""
    def __init__(self, size):
        """initializer"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """formatted output"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
