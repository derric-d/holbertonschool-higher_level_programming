#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    return([replace if i is search else i for i in newlist])
