# !/bin/bash

if [ "$1" = "1" ]; then
    #run the tests for doubly linked
    pytest test_linked_list.py --durations=0 "$2"

elif [ "$1" = "2" ]; then
    #run the tests for dynamic array
    pytest test_dynamic_array.py --durations=0 "$2"
fi

