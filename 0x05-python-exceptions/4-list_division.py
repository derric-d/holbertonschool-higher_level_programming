#!/usr/bin/python3


def list_division(l1, l2, list_length):
    ret = []
    if list_length > 0:
        for i in range(list_length):
            try:
                ret.append(l1[i] / l2[i])
            except TypeError:
                ret.append(0)
                print("wrong type")
            except ZeroDivisionError:
                ret.append(0)
                print("disvision by zero")
            except IndexError:
                ret.append(0)
                print("out of range")
            finally:
                pass
    return ret
