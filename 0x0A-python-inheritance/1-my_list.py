#!/usr/bin/python3
"""my list class"""


class MyList(list):
    """class"""

    def print_sorted(self):
        """print sorted"""
        print(sorted(self))
