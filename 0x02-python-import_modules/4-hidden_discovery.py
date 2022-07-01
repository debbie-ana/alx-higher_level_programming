#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    arr = dir(hidden_4)
    arr.sort()
    for fname in arr:
        if fname[:2] != "__":
            print("{}".format(fname))
