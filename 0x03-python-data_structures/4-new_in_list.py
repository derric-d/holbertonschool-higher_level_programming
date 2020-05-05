#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    if my_list:
        new_list = []
        for i, ele in enumerate(my_list):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(ele)
    return new_list
