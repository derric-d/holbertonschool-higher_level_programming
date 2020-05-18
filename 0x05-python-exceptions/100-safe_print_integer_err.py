#!/usr/bin/python3
from sys import stderr as SE


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception: {}".format(error), file=SE)
        return False
    else:
        return True
