#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arr = dir(hidden_4)
    arr.sort()
    for name in arr:
        if name[:2] != "__":
            print("{}".format(name))
