# Import helper libraries
# import random
# import sys
# import time
# import argparse

# import doubly linked list
from structures.linked_list import DoublyLinkedList as DL

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

    return my_list

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
    assert dll.get_head() == 3
    assert dll.get_tail() == 6

    # Test removing nodes from the back
    dll.remove_from_back()
    assert dll.get_size() == 2
    assert dll.get_head() == 3
    assert dll.get_tail() == 4

    # Test removing all nodes
    dll.remove_from_front()
    dll.remove_from_front()
    assert dll.get_size() == 0
    assert dll.get_head() is None
    assert dll.get_tail() is None

# testing str(my_list)
def test_string_1():
    my_list = set_up(0)
    print(my_list)
    assert(str(my_list) == "<>")

def test_string_2():
    my_list = set_up(1)
    assert(str(my_list) == "<Hello, World!>")

def test_string_3():
    my_list = set_up(3)
    assert(str(my_list) == "<Hello, World!>")

def test_string_4():
    my_list = set_up(2)
    assert(str(my_list) == "<4, 3, 2, 1>")

# testing getting the size
def test_size_1():
    my_list = set_up(0)
    assert(my_list.get_size() == 0)

def test_size_2():
    my_list = set_up(1)
    assert(my_list.get_size() == 2)

def test_size_3():
    my_list = set_up(2)
    assert(my_list.get_size() == 4)

# testing get_head()
def test_get_ends_1():
    my_list = set_up(0)
    assert(my_list.get_head() is None)
    assert(my_list.get_tail() is None)

def test_get_ends_2():
    my_list = set_up(1)
    assert(my_list.get_head() == "Hello")
    assert(my_list.get_tail() == "World!")

def test_get_ends_3():
    my_list = set_up(2)
    assert(my_list.get_head() == 4)
    assert(my_list.get_tail() == 1)

def test_get_ends_4():
    my_list = set_up(3)
    assert(my_list.get_head() == "Hello")
    assert(my_list.get_tail() == "World!")

# === Testing mroe advanced stuff === 
"""
inset_to_front -> inserts new node in the front with given data
inset_to_back -> inserts new node in the back with given data

"""

# testing insert to front
# 
# testing insert to back
#
# testing remove to front
#
# testing remove to back
#
# testing finding the element
# def test_find_elem_1():
#     my_list = set_up(2)
#     assert(my_list.find_element(1) == True)
#
# # testing find and remove elem
# def test_find_and_remove_1():
#     my_list = set_up(2)
#     assert(my_list.find_and_remove_element(2) == True)
#
# def test_find_and_remove_2():
#     my_list = set_up(2)
#     assert(my_list.find_and_remove_element(29) == False)
#
# testing reverse
#
