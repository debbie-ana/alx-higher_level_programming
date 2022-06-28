#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if (ord(a) >= 97 and ord(a) <= 122):
            print("{0:c}".format(ord(a) - 32), end="")
        else:
            print("{0:c}".format(ord(a)), end="")
    print("")
