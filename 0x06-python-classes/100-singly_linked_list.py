#!/usr/bin/python3
"""module for defining a singly linked list"""


class Node:
    """Node class
    Attributes:
        data (int): data for the node
        next_node (Node): points to next node
    """

    def __init__(self, data, next_node=None):
        """initializing the class
        Args:
            data (int): data for the node
            next_node (Node): next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter to set data
        Args:
            value (int): value to set data to
        """
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """property to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter to set next node
        Args:
            value (Node): value to set next node to
        """
        if (value is None) or (type(value) == Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initializing the class SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList.
        sorts the node as it is inserted
        Args:
            value (Node): The new node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
