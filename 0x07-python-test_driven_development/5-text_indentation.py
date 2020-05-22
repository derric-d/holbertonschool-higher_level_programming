#!/usr/bin/python3
"""
print newline after ".:?"
"""

def text_indentation(text):
    """
    text should be split by 2 newlines after one of ".:?"
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    l = len(text)
    line = ""

    for lett in text:
        if lett in [".", ":", "?"]:
            line += lett
            print(line.strip(" "), end='\n\n')
            line = ""
        else:
            line += lett

    print(line.strip(" "), end ="")
