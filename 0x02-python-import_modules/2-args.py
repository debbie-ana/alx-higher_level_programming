#!/usr/bin/python3
if __name__ != "__2-args__":
    import sys
    if (len(sys.argv) == 1):
        print("{0} arguments.".format(len(sys.argv) - 1))
    else:
        if (len(sys.argv) == 2):
            print("{0} argument:".format(len(sys.argv) - 1))
        else:
            print("{0} arguments:".format(len(sys.argv) - 1))
        i = 1
        while (i < len(sys.argv)):
            print("{0}: {1}".format(i, sys.argv[i]))
            i = i + 1
