# !/bin/bash

if [ "$11" = "11" ]; then
    #run the tests for doubly linked
    pytest test_linked_list.py "$2"

elif [ "$1" = "12" ]; then
    #run the tests for dynamic array
    pytest test_linked_list.py --durations=0 "$2"

elif [ "$1" = "21" ]; then
    #run the tests for dynamic array
    pytest test_dynamic_array.py "$2"

elif [ "$1" = "22" ]; then
    #run the tests for dynamic array
    pytest test_dynamic_array.py --durations=0 "$2"
fi

