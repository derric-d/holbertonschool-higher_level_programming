#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    if len(av) == 1:
        print("0 arguments.")
    elif len(av) == 2:
        print("{} argument:".format(len(av) - 1))
    else:
        print("{} arguments:".format(len(av) - 1))
    for i in range(len(av) - 1):
        print("{}: {}".format(i + 1, av[i + 1]))
