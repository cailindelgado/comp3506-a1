"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any
import math

#from dynamic_array import DynamicArray
from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism.
        We also track how many elements we are storing, an offset into each
        of the end integers, and states for reversed/flipped.
        """
        self._data = DynamicArray()
        self._size = 0
        self._left_offset = 64
        self._right_offset = -1
        self._reversed = False
        self._flipped = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bits = ""
        for i in range(self._size):
            bits += str(self.get_at(i))
        return bits

    def __repr__(self):
        return self.__str__()

    def __resize(self) -> None:
        pass

    def allocate(self, bits_desired: int) -> None:
        """
        Allow the user to allocate a slab of bits at once, all initialized
        to zero.
        """
        # Ceil division, see: https://stackoverflow.com/q/14822184/
        ints_required = -(bits_desired // -self.BITS_PER_ELEMENT)
        self._data.allocate(ints_required, 0)
        self._size = bits_desired
        self._left_offset = 64
        
        ptr = bits_desired % self.BITS_PER_ELEMENT

        if ptr == 0:
            self._right_offset = -1
        else:
            self._right_offset = self.BITS_PER_ELEMENT - ptr - 1 
        
        self._reversed = False
        self._flipped = False


    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        # 1: Check bounds
        if index < 0 or index >= self._size:
            return

        # 2: Get the int of interest
        if self._reversed:
            index = self._size - index - 1

        bit = self.__get(index)
        if self._flipped:
            bit = 1 - bit 
        return bit

    def __get(self, index: int) -> int:
        """
        Get a bit at a given position regardless of reversed and flipped.
        """
        adjusted_ix = index + (self.BITS_PER_ELEMENT - self._left_offset)

        data_ix = adjusted_ix // self.BITS_PER_ELEMENT

        bit_ix = self.BITS_PER_ELEMENT - (adjusted_ix % self.BITS_PER_ELEMENT) - 1
    
        bit = self._data[data_ix] & (1 << bit_ix)
        
        if bit != 0:
            bit = 1
        
        return bit

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
        self.__setitem__(index, 1)

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        self.__setitem__(index, 0)

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        
        if index < 0 or index >= self._size:
            return

        if state != 0:
            state = 1
        if self._flipped:
            state = 1 - state
        if self._reversed:
            index = self._size - index - 1

        self.__assign(index, state)

    # set a bit into a state regardless of reversed and flipped flags
    def __assign(self, index: int, state: int) -> None:
        adjusted_ix = index + (self.BITS_PER_ELEMENT - self._left_offset)

        data_ix = adjusted_ix // self.BITS_PER_ELEMENT

        bit_ix = self.BITS_PER_ELEMENT - (adjusted_ix % self.BITS_PER_ELEMENT) - 1
    
        if state == 1:
            self._data[data_ix] |= (state << bit_ix)
        else:
            self._data[data_ix] |= (1 << bit_ix)
            self._data[data_ix] ^= (1 << bit_ix)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if state != 0:
            state = 1
        if self._flipped:
            state = 1 - state

        if self._reversed:
            self.__prepend(state)
        else:
            self.__append(state)


    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if state != 0:
            state = 1
        if self._flipped:
            state = 1 - state

        if self._reversed:
            self.__append(state)
        else:
            self.__prepend(state)

    # prepend to the left regardless of the reversed and flipped flags
    def __prepend(self, state: int) -> None:
        if self._left_offset >= self.BITS_PER_ELEMENT:
            self._left_offset = 0
            self._data.prepend(0)
        self._data[0] |= (state << self._left_offset)
        self._left_offset += 1
        self._size += 1 

    # append to the right regardless of the reversed and flipped flags
    def __append(self, state: int) -> None:
        if self._right_offset < 0:
            self._right_offset = self.BITS_PER_ELEMENT - 1
            self._data.append(0)
        last = self._data.get_size() - 1
        self._data[last] |= (state << self._right_offset)
        self._right_offset -= 1
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._reversed = not self._reversed 

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flipped = not self._flipped 

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """
        if self._size == 0 or dist == 0:
            return
        
        if abs(dist) >= self._size:
            for i in range(self._data.get_size()):
                self._data[i] = 0
            return

        if self._reversed:
            dist = -dist

        # 01101011  >> 3
        # 00001101


        # 01101011  << 3
        # 01011000

        if dist < 0:
            for i in range(self._size - 1, -dist - 1, -1):
                self[i] = self[i + dist]
            for i in range(-dist):
                self.unset_at(i)
        else:
            for i in range(self._size - dist):
                self[i] = self[i + dist]
            for i in range(self._size - dist, self._size):
                self.unset_at(i)


    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """
        if self._size == 0 or dist == 0:
            return

        if self._reversed:
            dist = -dist

        dist %= self._size

        # Average Number theory enjoyer's solution:
        #
        # Assume dist is positive. If it's not, subtract it from size. 
        # Left rotation by dist and right rotation by size - dist are identical.
        # If d = gcd(dist, size), where gcd is Greatest common factor (a.k.a highest common factor), then
        # rotation (a.k.a cyclic shift) is split into d independent cyclic shifts. 
        # A group of indices equal modulo d will form one such independent cycle.

        d = math.gcd(dist, self._size)

        for i in range(d):
            start = i
            buf = self[start]
            while True:
                self[start] = self[(start + dist) % self._size]
                if (start + dist) % self._size == i:
                    self[start] = buf
                    break
                start += dist
                start %= self._size

        # However, using a whole array to store intermediate results will also be accepted
        #helper = DynamicArray()

        ### fill the array with bits

        #for i in range(self._size):
        #    int_index = ... # index of the helper int
        #    bit_index = ... # index of the bit within the helper int
        #    self[i] = helper[int_index] & (1 << bit_index)


    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size

