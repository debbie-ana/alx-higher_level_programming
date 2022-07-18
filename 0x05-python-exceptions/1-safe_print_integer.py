#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
