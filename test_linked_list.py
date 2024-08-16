import pytest

from structures.linked_list import DoublyLinkedList as DL
from random import randrange as rr
from collections import deque

def set_up(check: int) -> DL:
    my_list = DL()

    if check == 0:
        return my_list
    elif check == 1:
        my_list.insert_to_front("Hello")
        my_list.insert_to_back("World!")

    elif check == 2:
        my_list.insert_to_front(1)
        my_list.insert_to_front(2)
        my_list.insert_to_front(3)
        my_list.insert_to_front(4)

    elif check == 3:
        my_list.insert_to_back("World!")
        my_list.insert_to_front("Hello")

    elif check == 4:

        for i in range(0, 1000):
            roll = rr(1, 6)
            if roll == 1:
                my_list.insert_to_front(i)
            elif roll == 2:
                my_list.insert_to_back(i)
            elif roll == 3:
                my_list.remove_from_back()
            elif roll == 4:
                my_list.remove_from_front()
            elif roll == 5:
                my_list.reverse()
    return my_list

            
def set_up_2(check: int) -> bool:
    canon = deque()
    pass


# ==== Testing Getters and Setters ==== 
"""
get_size -> self._size
get_head -> data in self._head
get_tail -> data in self._tail
set_head -> in = data, replaces self._head data with in
set_tail -> in = data, replaces self._tail data with in

"""
def test_basics():
    # Test initializing an empty list
    dll = DL()
    assert dll.get_size() == 0
    assert dll.get_head() is None
    assert dll.get_tail() is None

    # Test inserting nodes to the front
    dll.insert_to_front(1)
    assert dll.get_size() == 1
    assert dll.get_head() == 1
    assert dll.get_tail() == 1

    dll.insert_to_front(2)
    assert dll.get_size() == 2
    assert dll.get_head() == 2
    assert dll.get_tail() == 1

    # Test inserting nodes to the back
    dll.insert_to_back(3)
    assert dll.get_size() == 3
    assert dll.get_head() == 2
    assert dll.get_tail() == 3

    dll.insert_to_back(4)
    assert dll.get_size() == 4
    assert dll.get_head() == 2
    assert dll.get_tail() == 4

    # Test setting head and tail
    dll.set_head(5)
    assert dll.get_head() == 5
    assert dll.get_tail() == 4

    dll.set_tail(6)
    assert dll.get_head() == 5
    assert dll.get_tail() == 6

    # Test removing nodes from the front
    dll.remove_from_front()
    assert dll.get_size() == 3
    assert dll.get_head() == 1
    assert dll.get_tail() == 6

    # Test removing nodes from the back
    dll.remove_from_back()
    assert dll.get_size() == 2
    assert dll.get_head() == 1
    assert dll.get_tail() == 3

    # Test removing all nodes
    dll.remove_from_front()
    dll.remove_from_front()
    assert dll.get_size() == 0
    assert dll.get_head() is None
    assert dll.get_tail() is None

# testing str(my_list)
def test_string():
    dll = set_up(0)
    assert str(dll) == "<>" 

    # Testing with different set up for dll
    dll = set_up(1)
    assert str(dll) == "<Hello, World!>" 

    dll = set_up(3)
    assert str(dll) == "<Hello, World!>" 

    dll = set_up(2)
    assert str(dll) == "<4, 3, 2, 1>" 

def test_size_1():
    dll = set_up(0)
    assert dll.get_size() == 0 

    dll = set_up(1)
    assert dll.get_size() == 2 

    dll = set_up(2)
    assert dll.get_size() == 4 

def test_get_ends_1():
    # Testing getting each of the ends ddl empty
    dll = set_up(0)
    assert dll.get_head() is None 
    assert dll.get_tail() is None 

    # Testing ends works for insert front then back
    dll = set_up(1)
    assert dll.get_head() == "Hello" 
    assert dll.get_tail() == "World!" 

    # Testing inserting numbers
    dll = set_up(2)
    assert dll.get_head() == 4 
    assert dll.get_tail() == 1 

    # Testing ends works for insert back then front
    dll = set_up(3)
    assert dll.get_head() == "Hello" 
    assert dll.get_tail() == "World!" 

# Testing on empty dll
def test_basics_empty():
    dll = DL()
    assert dll.get_size() == 0
    assert dll.get_tail() is None
    assert dll.get_head() is None

    dll.set_head(1) 
    dll.set_tail(1) 
    assert dll.get_head() is None
    assert dll.get_tail() is None
    

# === Testing more advanced stuff === 
"""
inset_to_front -> inserts new node in the front with given data
inset_to_back -> inserts new node in the back with given data
"""

class TestLinkedList:

    @pytest.fixture
    def linked_list(self):
        return DL()

    def test_insert_to_front(self, linked_list):
        linked_list.insert_to_front(1)
        assert linked_list.get_head() == 1
        assert linked_list.get_tail() == 1
        assert linked_list.get_size() == 1

        linked_list.insert_to_front(2)
        assert linked_list.get_head() == 2
        assert linked_list.get_tail() == 1
        assert linked_list.get_size() == 2

    def test_insert_to_back(self, linked_list):
        linked_list.insert_to_back(1)
        assert linked_list.get_head() == 1
        assert linked_list.get_tail() == 1
        assert linked_list.get_size() == 1

        linked_list.insert_to_back(2)
        assert linked_list.get_head() == 1
        assert linked_list.get_tail() == 2
        assert linked_list.get_size() == 2

    def test_remove_from_front(self, linked_list):
        linked_list.insert_to_back(1)
        linked_list.insert_to_back(2)
        assert linked_list.remove_from_front() == 1
        assert linked_list.get_head() == 2
        assert linked_list.get_size() == 1

        assert linked_list.remove_from_front() == 2
        assert linked_list.get_head() is None
        assert linked_list.get_size() == 0

    def test_remove_from_back(self, linked_list):
        linked_list.insert_to_back(1)
        linked_list.insert_to_back(2)
        assert linked_list.remove_from_back() == 2
        assert linked_list.get_tail() == 1
        assert linked_list.get_size() == 1

        assert linked_list.remove_from_back() == 1
        assert linked_list.get_tail() is None
        assert linked_list.get_size() == 0

    def test_find_element(self, linked_list):
        linked_list.insert_to_back(1)
        linked_list.insert_to_back(2)
        linked_list.insert_to_back(3)
        assert linked_list.find_element(2) == True
        assert linked_list.find_element(4) == False

    def test_find_and_remove_element(self, linked_list):
        linked_list.insert_to_back(1)
        linked_list.insert_to_back(2)
        linked_list.insert_to_back(3)
        assert linked_list.find_and_remove_element(2) == True
        assert linked_list.get_size() == 2
        assert linked_list.find_and_remove_element(4) == False
        assert linked_list.get_size() == 2

    def test_reverse(self, linked_list):
        linked_list.insert_to_back(1)
        linked_list.insert_to_back(2)
        linked_list.insert_to_back(3)
        print(linked_list)
        linked_list.reverse()
        print(linked_list)
        assert linked_list.get_head() == 3
        assert linked_list.get_tail() == 1
        linked_list.reverse()
        assert linked_list.get_head() == 1
        assert linked_list.get_tail() == 3

if __name__ == '__main__':
    pytest.main()
