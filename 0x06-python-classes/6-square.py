#!/usr/bin/python3
"""square class main"""


class Square():
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Instance of class Square
    Arguments:
        @size: size of side of square"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(position[0]) != int) or (type(position[1]) != int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter of position
    Return:
            value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setter of the position
    Arguments:
        value: value of postion"""
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[0]) != int) or (type(value[1]) != int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ square made using the character #
            or a blank line if @size == 0"""
        if (self.size == 0):
            print("")
        else:
            for x in range(self.position[1]):
                print()
            for i in range(self.size):
                print((self.position[0] * " ") + ("#" * self.size))
