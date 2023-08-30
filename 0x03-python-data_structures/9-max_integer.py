#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    lar = my_list[0]
    for i in range(1, len(my_list)):
        if lar < my_list[i]:
            lar = my_list[i]
        else:
            continue
    return lar
