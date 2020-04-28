#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    cpy = ''
    for char in str:
        if n is not i:
            cpy += char
        i += 1
    return cpy
