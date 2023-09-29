#!/usr/bin/python3
"""locked class module"""


class LockedClass:
    """class with no class or object attribute"""

    def __setattr__(self, attr, value):
        """prevents user from creating new instance attributes,
        except if the new instance attribute is called first_name
        """
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(attr))
        self.__dict__.update({attr: value})
