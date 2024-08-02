"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        self._size = 0
        self._head = None
        self._tail = None

    #TODO Fix this
    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """

        out = "<"
        node = self._head
        if node:
            while node.get_next() != None:
                out += node.get_data()
                node = node.get_next()

        return out + ">"

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Node | None:
        """
        Return the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self._head

    def set_head(self, node: Node) -> None:
        """
        Replace the leftmost node in the list.
        Time complexity for full marks: O(1)
        """
        self._head = node

    def get_tail(self) -> Node | None:
        """
        Return the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self.tail

    def set_tail(self, node: Node) -> None:
        """
        Replace the rightmost node in the list.
        Time complexity for full marks: O(1)
        """
        self.tail = node

    """
    More interesting functionality now.
    """

#TODO: fix all the nasty stuff I've done in here


    def insert_to_front(self, node: Node) -> None:
        """
        Insert a node to the front of the list
        Time complexity for full marks: O(1)
        """
        # if empty Doubly

        # if head

        # if no head
        if self._head:
            self._head.set_prev(node)
            self._head = node
            self._size += 1
        else:
            self._head = node

    def insert_to_back(self, node: Node) -> None:
        """
        Insert a node to the back of the list
        Time complexity for full marks: O(1)
        """

        # if empty Doubly
        if self._tail == self._head:   # so both None or nodes
            pass


        # if tail
        if self._tail:
            self._tail.set_next(node)
            self._tail = node
            self._size += 1
        else:
            self._tail = node

        # if no tail

    def remove_from_front(self) -> Node | None:
        """
        Remove and return the front element
        Time complexity for full marks: O(1)
        """
        # if 0 items in list
        if self._size == 0:
            return

        # if only 1 item in list
        if self._size == 1:
            pass


        # if more than 1
        if self._size >= 2:
            out = self._head
            self.set_head(self._head.get_next())
            self._size -= 1
            return out

    def remove_from_back(self) -> Node | None:
        """
        Remove and return the back element
        Time complexity for full marks: O(1)
        """
        if self._size >= 2:
            out = self.tail
            self.set_tail(self._tail.get_prev())
            self._size -= 1
            return out

    def find_element(self, elem: Any) -> Any | None:
        """
        Looks at the data inside each node of the list and returns the
        node if it matches the input elem; returns None otherwise
        Time complexity for full marks: O(N)
        """
        if self.get_head():
            current = self.get_head()

            while current.get_next() != None:
                if current.get_data() == elem:
                    break
                else: 
                    current = current.get_next()

            return current.get_data()
        else:
            return None

    def find_and_remove_element(self, elem: Any) -> Any | None:
        """
        Finds, removes, and returns the first instance of elem
        (based on the node data) or returns None if the element is not found.
        Time complexity for full marks: O(N)
        """
        current = self.get_head()

        if current:
            while current.get_next() != None:  
                if current.get_data() == elem:
                    break
                else: 
                    current = current.get_next()

            if not current.get_next():
                current.get_prev().set_next(None)



            previous = current.get_prev()
            next = current.get_prev()

            previous.set_next(next)
            next.set_next(previous)


        return current.get_data()

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        # temp = self._head
        # self._head = self._tail
        # self.tail = temp

        self._head, self._tail = self._tail, self._head
        pass


