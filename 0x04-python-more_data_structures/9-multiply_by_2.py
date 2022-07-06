#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for a in a_dictionary:
        new_dict[a] = a_dictionary[a] * 2
    return new_dict
