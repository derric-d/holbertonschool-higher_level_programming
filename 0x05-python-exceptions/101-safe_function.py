#!/usr/bin/python3
from sys import stderr as SE


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=SE)
        ret = None
    finally:
        return ret
