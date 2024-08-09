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
        self._left = 2
        self._right = 2
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
        new_array = [None] * self.get_capacity()

        new_start = self._left - self._size_left
        new_end = self._right - self._size_right
        
        for idx in range(new_start, new_end + 1):  # range(a, b) -> [a,b) want [a,b]
            self._array[idx] = new_array[idx]

        self._array = new_array

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not ((-1 * self.get_size()) <= index < self.get_size()):
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
        if not ((-1 * self.get_size()) <= index < self.get_size()):
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

        self.set_at(self._right - self._size_right - 1, element)
        
    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        self._size_left += 1
        if self._left == self._size_left:
            self.__resize()

        self.set_at(self._left - self._size_left - 1, element)

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
        # new implementation
        leftovers_l = self._left - self._size_left
        leftovers_r = self._right - self._size_right

        out = index
        if index >= 0 and not self._reverse:
            out = index + (leftovers_l)

        if index < 0 and not self._reverse:
            out = index - (leftovers_r)

        if self._reverse and index >= 0:
            out = (-1 * index + 1) - (leftovers_r)

        if self._reverse and index < 0:
            out = (-1 * index + 1) + (leftovers_l)

        return out

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        found = False
        start = self._left - self._size_left
        end = self._right - self._size_right

        # print(f'starting at: {start}, ending at: {end + 1}')

        for idx in range(start, end + 1):  # go through the position the array is sitting in
            if not found and (self._array[idx] == element):
                found = True

                if idx > self._left:  # dealing with decreasing the size
                   self._size_right -= 1
                else:  # if on the other side or in middle then reduce known size on that side by 1
                    self._size_left -= 1

            if found:
                self._array[idx] = self._array[idx + 1]

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if self._array[index] == None:
            return 
        else:
            self.set_at(index, None)

        end = self._right - self._size_right  # the position of the final element of the array

        for idx in range(index, end + 1):
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
        if self.get_size() <= 1:
            return

        middle = self.get_size() // 2








