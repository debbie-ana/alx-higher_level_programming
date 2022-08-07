#!/usr/bin/python3
"""text indentation module"""



def text_indentation(text):
    """prints a text with 2 new lines after the characters
    ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for word in text:
        if flag == 0:
            if word == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if word == '?' or word == '.' or word == ':':
                print(word)
                print()
                flag = 0
            else:
                print(word, end="")
