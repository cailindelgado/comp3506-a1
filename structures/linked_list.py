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

    def set_next(self, node: Node | None, reverse: bool | None) -> None:
        if reverse:
            self._prev = node
        else:
            self._next = node

    def get_next(self, reverse: bool | None) -> Node | None:
        if reverse:
            return self._prev
        else:
            return self._next

    def set_prev(self, node: Node | None, reverse: bool | None) -> None:
        if reverse:
            self._next = node
        else:
            self._prev = node

    def get_prev(self, reverse: bool | None) -> Node | None:
        if reverse:
            return self._next
        else:
            return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec]
    """

    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        out = "<"
        current = self._head

        while current is not None:
            if current.get_next(self._reverse) == None:
                out += f"{current.get_data()}"
            else:
                out += f"{current.get_data()}, "

            current = current.get_next(self._reverse)
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

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if not self._reverse:
            if self._head:
                return self._head.get_data()
        else:
            if self._tail:
                return self._tail.get_data()

        return

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if not self._reverse:
            if self._head:
                self._head.set_data(data)
        else:
            if self._tail:
                return self._tail.set_data(data)

        return

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if not self._reverse:
            if self._tail:
                return self._tail.get_data()
        else:
            if self._head:
                return self._head.get_data()

        return

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if not self._reverse:
            if self._tail:
                self._tail.set_data(data)
        else:
            if self._head:
                self._head.set_data(data)

        return

    """
    More interesting functionality now.
    Note that any time you see 'Any' in the type annotations,
    this refers to the "data" stored inside a Node.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        new = Node(data)
        new.set_next(self._head, self._reverse)

        if self._head is not None:
            self._head.set_prev(new, self._reverse)

        if self._tail is None:
            self._tail = new

        self._head = new
        self._size += 1

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        new = Node(data)
        new.set_prev(self._tail, self._reverse)

        if self._tail is not None:
            self._tail.set_next(new, self._reverse)

        if self._head is None:
            self._head = new

        self._tail = new
        self._size += 1

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        out = self.get_head()

        # what happens when only 1 item in list
        if self.get_size() == 1:
            self._head = None
            self._tail = None
            self._size -= 1

        # what happens when more than one item in list
        if (self.get_size() >= 2) and (self._head is not None):
            # set the current head to be the second position
            self._head = self._head.get_next(self._reverse)
            self._size -= 1

        return out

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        out = self.get_tail()

        # what happens when only 1 item in list
        if self.get_size() == 1:
            self._head = None
            self._tail = None
            self._size -= 1

        # what happens when more than one item in list
        if (self.get_size() >= 2) and (self._tail is not None):
            self._tail = self._tail.get_prev(self._reverse)
            self._size -= 1

        return out

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        found = False
        current = self._head

        if current:
            while current is not None:
                if current.get_data() == elem:
                    found = True
                    break

                current = current.get_next(self._reverse)

        return found

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        found = False
        current = self._head

        if current:
            while current is not None:
                if current.get_data() == elem:
                    found = True
                    break

                current = current.get_next(self._reverse)

        if found and current:  # if found elem
            next = current.get_next(None)
            prev = current.get_prev(None)

            if next is not None and prev is not None:  # if current is in middle
                next.set_prev(prev, None)
                prev.set_next(next, None)
            elif next is None and prev is not None:  # if current is the tail
                prev.set_next(None, None)
                self._tail = prev
            elif next is not None and prev is None:  # if current is the head
                next.set_prev(None, None)
                self._head = next

            self._size -= 1

        return found

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        # flip the flag when reverse is called
        self._reverse = not self._reverse
