#!/usr/bin/python3
def remove_char_at(str, n):
    ns = ''
    for c in str:
        if (n == 0):
            n = n - 1
        else:
            ns = ns + c
        n = n - 1
    return (ns)
