#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    for i in range(0, len(d)):
        if d[i][0:2] != "__":
            print(d[i])
