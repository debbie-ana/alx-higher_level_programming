#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for a in my_string:
        if not(a == 'c' or a == 'C'):
            str += a
    return str
