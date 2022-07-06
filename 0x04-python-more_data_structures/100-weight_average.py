#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for t in my_list:
        average += t[0] * t[1]
        div += t[1]
    return float(average / div)
