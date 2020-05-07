#!/usr/bin/python3
def complex_delete(a_dic, value):
    for i in list(a_dic.keys()):
        if value == a_dic[i]:
            del(a_dic[i])
    return(a_dic)
