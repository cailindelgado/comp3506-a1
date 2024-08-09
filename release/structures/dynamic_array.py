"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

class DynamicArray:
    def __init__(self) -> None:
        """ 
        Create an empty array
        """
        self._size_left = 0
        self._size_right = 0
        self._left = 16
        self._right = 16
        self._array = [None] * (self._left + self._right)
        self._reverse = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        return str(self._array)

    def __resize(self) -> None:
        """
        Create a new section of "storage" to hold the data
        """
        self._left *= 2
        self._right *=  2
        new = [None] * (self.get_capacity() * 2)
        new_start = self._left - self._size_left
        new_end = self._right - self._size_right
        
        for idx in range(new_start, new_end + 1):  # range(a, b) -> [a,b) want [a,b]
            self._array[idx] = new[idx]

        self._array = new

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= abs(index) <= self.get_size():
            return
        return self._array[self.rev_values(index)]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(self.rev_values(index))

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= abs(index) <= self.get_size():
            return

        self._array[self.rev_values(index)] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        self._size_right += 1
        if self._right == self._size_right:
            self.__resize()

        self.set_at(self._right - self._size_right, element)
        
    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        self._size_left += 1

        if self._left == self._size_left:
            self.__resize()

        self.set_at(self._left - self._size_left, element)

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def rev_values(self, index: int) -> int:
        """
        Handles reversing the logic of the indexes of the array
        """
        leftovers = self.get_capacity() - self.get_size()
        out = abs(index)
        if self._reverse:
            out -= leftovers;
        return out

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        found = False
        for idx in range(self.get_size()):
            if self._array[idx] == element:
                found = True

            if found:
                self._array[idx] = self._array[idx + 1]

        self._size -= 1

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        self.set_at(index, None)
        for idx in range(index, self._size):
            self._array[idx] = self._array[idx + 1]

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self.get_size() == 0

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        return self.get_size() == self.get_capacity()

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size_left + self._size_right

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._left + self._right

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        # Merge sort
        middle = self.get_size() // 2
        # left = 





