"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any
from random import randrange as rr


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
        self._update = True 

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        return str(self._array)
        # out = "[ "
        # for i in range(self._left - self._size_left, self._left + self._size_right):
        #     out += f"{self._array[i]} "
        #
        # return out + "]"

    def __resize(self) -> None:
        """
        Create a new section of "storage" to hold the data
        """
        old_start = self._left - self._size_left
        old_end = self._left + self._size_right

        if self._update:  # if true, then increase size on left
            self._left *= 2
        else:
            self._right *= 2

        new_array = [None] * self.get_capacity()

        new_start = self._left - self._size_left

        for idx in range(old_start, old_end):  # [old_start, old_end) == [os, oe]
            new_array[new_start + idx - old_start] = self._array[idx]

        self._array = new_array

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (-1 * self.get_size()) <= index < self.get_size():
            return self._array[self.rev_values(index)]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (-1 * self.get_size()) <= index < self.get_size():
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
        if self._reverse:  # if reversed do a prepend (ran out of time for big brian sol)
            if self._left == self._size_left:
                self._update = True
                self.__resize()

            self._array[self._left - self._size_left - 1] = element
            self._size_left += 1
        else:
            if self._right == self._size_right:
                self._update = False
                self.__resize()

            self._array[self._left + self._size_right] = element
            self._size_right += 1

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._reverse:  # if reversed do an append
            if self._right == self._size_right:
                self._update = False
                self.__resize()

            self._array[self._left + self._size_right] = element
            self._size_right += 1
        else:
            if self._left == self._size_left:
                self._update = True
                self.__resize()

            self._array[self._left - self._size_left - 1] = element
            self._size_left += 1

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
        start = self._left - self._size_left
        end = self._left + self._size_right
        out = index

        if not self._reverse and index >= 0:
            out = index + start

        if not self._reverse and index < 0:
            out = end + index

        if self._reverse and index >= 0:
            out = end + (-1 * index - 1)

        if self._reverse and index < 0:
            out = (-1 * index) - 1 + start

        return out

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        found = False 
        fidx = 0

        for idx in range(0, self.get_size()):
            if (self.get_at(idx) == element) and not found:
                self.set_at(idx, None)
                found = True
                fidx = idx
                break

        if found:
            for idx in range(fidx, self.get_size() - 1):
                indx_A = self.rev_values(idx)
                indx_B = self.rev_values(idx + 1)

                self._array[indx_A], self._array[indx_B] = self._array[indx_B], self._array[indx_A]

            if self._reverse:
                self._size_left -= 1
            else:
                self._size_right -= 1

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None. 
        Time complexity for full marks: O(N)
        """
        out = self.get_at(index)

        if out == None:
            return

        self.set_at(index, None)

        # update size
        if self.rev_values(index) >= self._left:  # if on right half
            for idx in range(self.rev_values(index), self.get_capacity() - 1): # push in from right
                self._array[idx], self._array[idx + 1] = self._array[idx + 1], self._array[idx]

            if self.rev_values(index) - self.get_capacity() == 1:
                indx = self.rev_values(index)
                self._array[indx], self._array[indx + 1] = self._array[indx + 1], self._array[indx]

            self._size_right -= 1

        else:
            for idx in range(self.rev_values(index), 1, -1):
                self._array[idx], self._array[idx - 1] = self._array[idx - 1], self._array[idx]

            if self._left - self.rev_values(index) == self._left - 1:
                indx = self.rev_values(index)
                self._array[indx], self._array[indx - 1] = self._array[indx - 1], self._array[indx]

            self._size_left -= 1

        return out

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
        start = self._left - self._size_left
        end = self._left + self._size_right

        # array_parity = self._reverse
        # self._reverse = False

        self.qsort(self._array, start, end - 1)

        # self._reverse = array_parity

    def qsort(self, toSort: Any, start: int, end: int) -> None:
        """
        In place quick sort based on Lumoto's partition scheme with a random pivot
        """
        if start >= end:
            return

        # find a middle by splitting into a partition
        mid = self.partition(toSort, start, end)

        # recursively run qsort on other parts of array
        self.qsort(toSort, start, mid - 1)
        self.qsort(toSort, mid + 1, end)

    def partition(self, part: Any, start: int, end: int) -> int:
        """
        Helper function for qsort, which partitions the array
        into two unsorted sections to be sorted
        """
        # swap a random element to be a pivot with the last element
        indx = rr(start, end + 1)
        part[end], part[indx] = part[indx], part[end]

        pivot = part[end]
        pivot_pos = start - 1
        for j in range(start, end):  # [start, end - 1]
            if part[j] <= pivot:
                pivot_pos += 1
                part[pivot_pos], part[j] = part[j], part[pivot_pos]

        part[pivot_pos + 1], part[end] = part[end], part[pivot_pos + 1]  # put the pivot into place

        return pivot_pos + 1
