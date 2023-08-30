#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    result = 0
    result2 = 0
    for a, b in my_list:
        reult += a * b
        result2 += b
    return (result / result2)
