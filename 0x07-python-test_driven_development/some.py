#!/usr/bin/python3
The ``5-text_indentation`` module 
 ====================== 
  
 Using ``text_indentation``
----------------------------------------------
Checking for module docstring:
    >>> md = __import__("5-text_indentation").__doc__
    >>> len(md) > 1
    True

Importing the function from the module
>>> text_indentation = __import__("5-text_indentation").text_indentation

Checking for function docstring:
    >>> fd = __import__("5-text_indentation").text_indentation.__doc__
    >>> len(fd) > 1
    True

Test (text is string):
    >>> text_indentation("hello .How are you? ")
    hello .

    How are you?


Test (text is not string):
    >>> text_indentation(9)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string

Test (string with blank line):
    >>> text_indentation("what a great day.\n")
    what a great day.




Test (missing one argument):
    >>> text_indentation()
    Traceback (most recent call last):
    ...
    TypeError: text_indentation() missing 1 required positional argument: 'text'
