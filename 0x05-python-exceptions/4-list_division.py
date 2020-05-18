#!/usr/bin/python3
def list_division(l1, l2, llen):
    reslist = []
    ele = 0
    div = 0
    while i < llen:
        try:
            ret.append(l1[ele] / l2[ele])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            reslist.append(div)
            i += 1
    return reslist
