# !/bin/bash

if [ "$1" = "11" ]; then # run the tests for doubly linked list
    pytest test_linked_list.py "$2"
elif [ "$1" = "12" ]; then
    pytest test_linked_list.py --durations=0 "$2"

elif [ "$1" = "21" ]; then # run the tests for dynamic array
    pytest test_dynamic_array.py "$2"
elif [ "$1" = "22" ]; then 
    pytest test_dynamic_array.py --durations=0 "$2"

elif [ "$1" = "31" ]; then # run the tests for bit vector
    pytest test_bit_vector.py "$2"
elif [ "$1" = "32" ]; then
    pytest test_bit_vector.py --durations=0 "$2"

elif [ "$1" = "4" ]; then # run the tests for warmup
    pytest test_warmup.py "$2"
fi

