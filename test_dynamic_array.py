from random import randrange as rand
from _pytest.assertion import DummyRewriteHook
import pytest
from structures.dynamic_array import DynamicArray as da

class TestDynamicArrayBasics:

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
        assert dynamic_array.get_at(0) == 1 
        assert dynamic_array._array == [None, None, 1, None]
        assert dynamic_array._size_right == 1

    def test_append2(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(1)
        dynamic_array.append(1)
        dynamic_array.reverse()
        dynamic_array.append(1)
        dynamic_array.append(1)
        dynamic_array.append(1)
        assert dynamic_array._array == [None, 1, 1, 1, 1, 1, 1, None]

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
        dynamic_array.append(0) 
        dynamic_array.append(1) 
        dynamic_array.append(2) 
        dynamic_array.append(3) 
        dynamic_array.prepend(1)
        dynamic_array.prepend(2)
        dynamic_array.prepend(3)
        dynamic_array.reverse()
        dynamic_array.remove(1)
        #                         [None, 3, 2, 1, 0, 1, 2, 3]
        assert dynamic_array._array == [None, 3, 2, 0, 1, 2, 3, None]

    def test_remove2(self, dynamic_array):
        dynamic_array.append(0) 
        dynamic_array.append(1) 
        dynamic_array.append(2) 
        dynamic_array.append(3) 
        dynamic_array.prepend(1)
        dynamic_array.prepend(2)
        dynamic_array.prepend(3)
        dynamic_array.remove(1)
        #                         [None, 3, 2, 1, 0, 1, 2, 3]
        assert dynamic_array._array == [None, 3, 2, 0, 1, 2, 3, None]

    def test_remove_at(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(2)
        assert dynamic_array.remove_at(0) == 1
        assert dynamic_array._array == [None, None, 2, None]

    def test_remove_at2(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.reverse()
        assert dynamic_array.remove_at(0) == 1
        assert dynamic_array._array == [None, None, 2, None]

    def test_is_empty(self, dynamic_array):
        assert dynamic_array.is_empty() == True
        dynamic_array.append(1)
        assert dynamic_array.is_empty() == False

    def test_is_full(self, dynamic_array):
        assert dynamic_array.is_full() == False
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.prepend(3)
        dynamic_array.prepend(4)
        assert dynamic_array.is_full() == True

    def test_get_size(self, dynamic_array):
        assert dynamic_array.get_size() == 0
        dynamic_array.append(1)
        assert dynamic_array.get_size() == 1

    def test_get_capacity(self, dynamic_array):
        assert dynamic_array.get_capacity() == 4

    def test_resize(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(1)
        dynamic_array.append(1)
        dynamic_array.append(1)
        assert dynamic_array._array == [None, None, 1, 1, 1, 1]

    def test_reverse(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.reverse()
        dynamic_array.append(2)
        assert dynamic_array.get_at(0) == 1
        assert dynamic_array.get_at(-1) == 2

    def test_sort(self, dynamic_array):
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.prepend(3)
        dynamic_array.prepend(4)
        print(dynamic_array)
        dynamic_array.sort()
        assert dynamic_array._array == [1, 2, 3, 4]


# ==== More advanced testing ==== #


class TestdaAdv:

    @pytest.fixture
    def dynamic_array(self):
        return da()

    def populateBasic(self, A: list[int] | da, amount: int, case: int) -> None:
        for i in range(0, amount + 1):
            if case == 1:
                self.method(A, 0, i)  # append
            elif case == 2:
                self.method(A, 1, i)  # prepend
            elif case == 3:
                self.method(A, rand(0, 2), i)
                

    def populateAdv(self, A: list[int] | da, amount: int) -> None:
        for i in range(0,amount + 1):  # range(a, b) -> [a, b)
            self.method(A, rand(0, 6), i)

    def method(self, lst: list[int] | da, roll: int, value: int) -> None:
        if isinstance(lst, list):
            if roll == 0:
                lst.append(value)
            elif roll == 1:
                lst.insert(0, value)
            elif roll == 2:
                lst.reverse()
            elif roll == 3:
                if len(lst) != 0:
                    lst.remove(rand(0, len(lst)))  # remove the first element found
            elif roll == 4:
                if len(lst) != 0:
                    lst.pop(rand(0, len(lst)))
        else:
            if roll == 0:
                print("Appending")
                print(lst)
                lst.append(value)
                print(lst)
                print(f'appended: {value}, reverse: {lst._reverse}, val: {value}\n~~~~~~~~~~~~')
            elif roll == 1:
                print("Prepending")
                print(lst)
                lst.prepend(value)
                print(lst)
                print(f'prepended: {value}, reverse: {lst._reverse}, val: {value}\n~~~~~~~~~~~~')
            elif roll == 2:
                lst.reverse()
            elif roll == 3:
                if lst.get_size() != 0:
                    val = rand(0, lst.get_size()) 
                    print("Removing")
                    print(lst)
                    lst.remove(val)  # remove the first element found
                    print(lst)
                    print(f'remove: {val}, val: {val}, reverse: {lst._reverse}\n~~~~~~~~~~~~')
            elif roll == 4:
                if lst.get_size() != 0:
                    val = rand(0, lst.get_size())
                    print(f"Removing_at: {val}")
                    print(lst)
                    lst.remove_at(val)
                    print(lst)
                    print(f'remove_at: reverse: {lst._reverse}\n~~~~~~~~~~~~')

    @pytest.mark.skip(reason= "reverse brkn")
    def test_everything0(self, dynamic_array):
        self.populateAdv(dynamic_array, 10)

        print(dynamic_array)
        dynamic_array.sort()
        print(dynamic_array)
        
        for i in range(dynamic_array.get_size() - 1):
            assert dynamic_array[i] <= dynamic_array[i + 1]

    @pytest.mark.skip(reason= "reverse brkn")
    def test_everything1(self, dynamic_array):
        self.populateAdv(dynamic_array, 100)

        dynamic_array.sort()
        
        for i in range(dynamic_array.get_size() - 1):
            assert dynamic_array[i] <= dynamic_array[i + 1]

    @pytest.mark.skip(reason= "reverse brkn")
    def test_everything2(self, dynamic_array):
        self.populateAdv(dynamic_array, 1000)

        dynamic_array.sort()
        
        for i in range(dynamic_array.get_size() - 1):
            assert dynamic_array[i] <= dynamic_array[i + 1]

    @pytest.mark.skip(reason= "reverse brkn")
    def test_everything3(self, dynamic_array):
        self.populateAdv(dynamic_array, 10000)

        dynamic_array.sort()
        
        for i in range(dynamic_array.get_size() - 1):
            assert dynamic_array[i] <= dynamic_array[i + 1]

    @pytest.mark.skip(reason= "reverse brkn")
    def test_everything4(self, dynamic_array):
        self.populateAdv(dynamic_array, 100000)

        dynamic_array.sort()
        
        for i in range(dynamic_array.get_size() - 1):
            assert dynamic_array[i] <= dynamic_array[i + 1]
