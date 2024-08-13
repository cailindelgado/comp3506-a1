import pytest
from structures.dynamic_array import DynamicArray as da

# create a function for generating a list/array of a certain size and then randomsize the inputs. 
# for large functions


class TestDynamicArray:

    @pytest.fixture
    def dynamic_array(self):
        return da()

    def test_init(self, dynamic_array):
        assert dynamic_array._size_left == 0
        assert dynamic_array._size_right == 0
        assert dynamic_array._left == 2
        assert dynamic_array._right == 2
        assert dynamic_array._array == [None, None, None, None]
        assert dynamic_array._reverse == False

    def test_append(self, dynamic_array):
        dynamic_array.append(1)
        assert dynamic_array._array == [None, None, 1, None]
        assert dynamic_array._size_right == 1

    def test_prepend(self, dynamic_array):
        dynamic_array.prepend(1)
        assert dynamic_array._array == [None, 1, None, None]
        assert dynamic_array._size_left == 1

    def test_get_at(self, dynamic_array):
        dynamic_array.append(1)
        assert dynamic_array.get_at(0) == 1
        assert dynamic_array.get_at(1) == None

    def test_set_at(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.set_at(0, 2)
        assert dynamic_array._array == [None, None, 2, None]

    def test_remove(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.remove(1)
        assert dynamic_array._array == [None, None, 2, None]

    def test_remove_at(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.remove_at(0)
        assert dynamic_array._array == [None, None, 2, None]

    def test_is_empty(self, dynamic_array):
        assert dynamic_array.is_empty() == True
        dynamic_array.append(1)
        assert dynamic_array.is_empty() == False

    # def test_is_full(self, dynamic_array):
    #     assert dynamic_array.is_full() == False
    #     dynamic_array.append(1)
    #     dynamic_array.append(2)
    #     dynamic_array.append(3)
    #     dynamic_array.append(4)
    #     assert dynamic_array.is_full() == True

    def test_get_size(self, dynamic_array):
        assert dynamic_array.get_size() == 0
        dynamic_array.append(1)
        assert dynamic_array.get_size() == 1

    def test_get_capacity(self, dynamic_array):
        assert dynamic_array.get_capacity() == 4

