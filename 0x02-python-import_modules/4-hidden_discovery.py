#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    d.sort()
    for fname in d:
        if fname[:2] != "__":
            print(fname, end="\n")
