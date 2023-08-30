#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        numb = 0
        dem = 0
        for tupl in my_list:
            numb += (tupl[0] * tupl[1])
            dem += tupl[1]
        return (numb / dem)
    return 0
