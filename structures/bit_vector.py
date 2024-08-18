"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64  # range of each element is [0, 2^64 - 1]

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        self._LSB = 0  # Position of the Leftmost bit 
        self._MSB = 0  # Position of the Rightmost bit

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        return str(self._data)

    def __resize(self) -> None:
        pass

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if 0 <= (index//self.BITS_PER_ELEMENT) < self._data.get_size():
            out = self._data[index//self.BITS_PER_ELEMENT]
            if out is not None:
                out &= 1>>(index % 64)
                return 1 if out != 0 else out

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if 0 <= (index//self.BITS_PER_ELEMENT) < self._data.get_size():
            out = self._data[index//self.BITS_PER_ELEMENT]
            if out is not None:
                out |= 1>>(index % 64)
                self._data[index//self.BITS_PER_ELEMENT] = out

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if 0 <= (index//self.BITS_PER_ELEMENT) < self._data.get_size():
            out = self._data[index//self.BITS_PER_ELEMENT]
            if out is not None:
                out &= ~ (1>>(index % 64))
                self._data[index//self.BITS_PER_ELEMENT] = out

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if state:
            self.set_at(index)
        else: 
            self.unset_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._data.get_part(True) == self._MSB // self.BITS_PER_ELEMENT:
            self._data.append(0)

        self.__setitem__(self._MSB, state)
        self._MSB += 1

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._LSB == -64:
            self._data.prepend(2**63)
            self._MSB += 64
        else:
            self.__setitem__(64 + self._LSB, state)
            self._LSB -= 1
            

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        pass

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        pass

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return 0
