#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class with base inheritance """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of rectangle """
        return self.__width

    @property
    def height(self):
        """ height of rectangle """
        return self.__height

    @property
    def x(self):
        """ horizontal offset """
        return self.__x

    @property
    def y(self):
        """ vertical offset """
        return self.__y

    @width.setter
    def width(self, value):
        """ set width of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ rectangle made using the character #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.y):
            print()
        for row in range(self.__height):
            if row < (self.__height - 1):
                print((self.x * " ") + ("#" * self.__width))
            else:
                print((self.x * " ") + ("#" * self.__width))

    def __str__(self):
        """ staright printed value of instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ update attribute value """
        a = ["id", "width", "height", "x", "y"]
        if len(args) != 0 and args is not None:
            for i in range(len(args)):
                if i > len(a) - 1:
                    break
                setattr(self, a[i], args[i])
        else:
            for i in kwargs.keys():
                if i in a:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """ list representation of instance """
        temp = {}
        a = ["id", "width", "height", "x", "y"]
        for i in a:
            temp[i] = getattr(self, i)
        return temp
