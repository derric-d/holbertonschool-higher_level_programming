#!/usr/bin/python3
def uppercase(str):
    for i in str:
        tmp = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            tmp -= 32
        print("{:c}".format(tmp), end='')
    print('')
