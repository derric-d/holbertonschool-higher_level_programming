#!/usr/bin/python3
def roman_to_int(roman_str):
    if type(roman_str) == str:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        n = 0
        for i in roman_str:
            if dic[i] > n:
                val += dic[i] - n * 2
            else:
                val += dic[i]
            n = dic[i]
        return (val)
    return 0
