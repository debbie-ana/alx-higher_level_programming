#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        l = list(a_dictionary)
        best = 0
        for a in l:
            if a_dictionary[a] > best:
                best = a_dictionary[a]
                a_dict = a
        return a_dict
