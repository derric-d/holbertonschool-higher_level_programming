#!/usr/bin/python3
"""rec module"""
from  models.base import Base


class Rectangle(Base):
    """rec class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """h"""
        return self.__height

    @height.setter
    def height(self, height):
        """height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """x get"""
        return self.__x

    @x.setter
    def x(self, x):
        """x set"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """y get"""
        return self.__y

    @y.setter
    def y(self, y):
        """y set"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """area"""
        return self.width * self.height

    def display(self):
        """disp"""
        rows = self.width
        cols = self.height
        for y in range(self.y):
            print()
        for c in range(cols):
            for x in range(self.x):
                print(' ', end='')
            for r in range(rows):
                print('#', end='')
            print()

    def __str__(self):
        """doc"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update"""
        if args is not None and len(args) != 0:
            n_arg = len(args)
            if n_arg >= 1:
                self.id = args[0]
            if n_arg >= 2:
                self.width = args[1]
            if n_arg >= 3:
                self.height = args[2]
            if n_arg >= 4:
                self.x = args[3]
            if n_arg >= 5:
                self.id = args[4]
        elif kwargs is not None and len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """to dic"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
