#!/usr/bin/python3
"""module square for the module that holds the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class sqr, for the class of square,
    has getters setters, inherits from base>>rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """update"""
        if args is not None and len(args) != 0:
            n_arg = len(args)
            if n_arg >= 1:
                self.id = args[0]
            if n_arg >= 2:
                self.size = args[1]
            if n_arg >= 3:
                self.x = args[2]
            if n_arg >= 4:
                self.y = args[3]
        elif kwargs is not None and len(kwargs) != 0:
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, val):
        """size"""
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        self.width = val
        self.height = val

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}"\
        .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """to dic"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
