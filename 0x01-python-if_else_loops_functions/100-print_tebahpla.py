#!/usr/bin/python3
str = ''
for i in range(25, -1, -1):
    if (i % 2 == 0):
        str = str + chr(i + 65)
    else:
        str = str + chr(i + 97)
print("{0}".format(str), end="")
