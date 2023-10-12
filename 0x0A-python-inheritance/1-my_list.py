#!/usr/bin/python3
"""class that inherits from list"""

class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        "prints sorted list in ascending order"
        print(sorted(self))
