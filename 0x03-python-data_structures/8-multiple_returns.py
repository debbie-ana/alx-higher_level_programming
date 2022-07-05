#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence:
        i = sentence[0]
    else:
        i = None
    return (l, i)
