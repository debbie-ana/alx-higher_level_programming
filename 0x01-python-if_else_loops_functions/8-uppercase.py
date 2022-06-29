#!/usr/bin/python3
def uppercase(str):
    strn = ''
    for a in str:
        if (ord(a) >= 97 and ord(a) <= 122):
            strn = strn + chr(ord(a) - 32)
        else:
            strn = strn + a
    print("{0}".format(strn))
