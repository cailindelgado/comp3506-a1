"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

WARMUP PROBLEMS

 Each problem will be assessed on three sets of tests:

1. "It works":
       Basic inputs and outputs, including the ones peovided as examples, with generous time and memory restrictions.
       Large inputs will not be tested here.
       The most straightforward approach will likely fit into these restrictions.

2. "Exhaustive":
       Extensive testing on a wide range of inputs and outputs with tight time and memory restrictions.
       These tests won't accept brute force solutions, you'll have to apply some algorithms and optimisations.

 3. "Welcome to COMP3506":
       Extensive testing with the tightest possible time and memory restrictions
       leaving no room for redundant operations.
       Every possible corner case will be assessed here as well.

There will be hidden tests in each category that will be published only after the assignment deadline.
"""

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node


def main_character(instring: list[int]) -> int:
    """
    @instring@ is an array of integers in the range [0, 2^{32}-1].
    Return the first position a repeat integer is encountered, or -1 if
    there are no repeated ints.

    Limitations:
        "It works":
            @instring@ may contain up to 10'000 elements.

        "Exhaustive":
            @instring@ may contain up to 300'000 elements.

        "Welcome to COMP3506":
            @instring@ may contain up to 5'000'000 elements.

    Examples:
    main_character([1, 2, 3, 4, 5]) == -1
    main_character([1, 2, 1, 4, 4, 4]) == 2
    main_character([7, 1, 2, 7]) == 3
    main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1
    """

    """
    Approach: Use a big-ass (TM) bitvector to track characters we've seen
    We back out as soon as we find a bit that's already set
    O(n) worst case time where all elements in the input are unique
    """
    chars_seen = BitVector()
    chars_seen.allocate(2**32)
    for idx, char in enumerate(instring):
        if chars_seen.get_at(char) == 1:
            return idx
        chars_seen.set_at(char)
    return -1


def missing_odds(inputs: list[int]) -> int:
    """
    @inputs@ is an unordered array of distinct integers.
    If @a@ is the smallest number in the array and @b@ is the biggest,
    return the sum of odd numbers in the interval [a, b] that are not present in @inputs@.
    If there are no such numbers, return 0.

    Limitations:
        "It works":
            @inputs@ may contain up to 10'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^4
        "Exhaustive":
            @inputs@ may contain up to 300'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^6
        "Welcome to COMP3506":
            @inputs@ may contain up to 5'000'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^16

    Examples:
    missing_odds([1, 2]) == 0
    missing_odds([1, 3]) == 0
    missing_odds([1, 4]) == 3
    missing_odds([4, 1]) == 3
    missing_odds([4, 1, 8, 5]) == 10    # 3 and 7 are missing
    """

    """
    Approach: Make a linear pass over the list. While making that pass, track
    the lowest and highest value to get our range of interest, and also track
    the sum of odd values oberved. Then, simply find out the sum of odds in
    the range of interest, subtract the odds we did have, and the result is
    the sum of the missing odds.
    O(n) in the input array size.
    """
 
    upper = 0
    lower = 10000000000000000 # 10**16
    sum_of_odds = 0
    for element in inputs:
        # could use min or max here
        if element < lower:
            lower = element
        if element > upper:
            upper = element
        if element % 2 == 1:
            sum_of_odds += element

    if lower % 2 == 0:
        lower += 1
    if upper % 2 == 0:
        upper -= 1

    sum_of_odds_in_range = (upper + lower) * (upper - lower + 2) // 4
    return sum_of_odds_in_range - sum_of_odds


def k_cool(k: int, n: int) -> int:
    """
    Return the n-th largest k-cool number for the given @n@ and @k@.
    The result can be large, so return the remainder of division of the result
    by 10^16 + 61 (this constant is provided).

    Limitations:
        "It works":
            2 <= k <= 128
            1 <= n <= 10000
        "Exhaustive":
            2 <= k <= 10^16
            1 <= n <= 10^100     (yes, that's ten to the power of one hundred)
        "Welcome to COMP3506":
            2 <= k <= 10^42
            1 <= n <= 10^100000  (yes, that's ten to the power of one hundred thousand)

    Examples:
    k_cool(2, 1) == 1                     # The first 2-cool number is 2^0 = 1
    k_cool(2, 3) == 2                     # The third 2-cool number is 2^1 + 2^0 = 3
    k_cool(3, 5) == 10                    # The fifth 3-cool number is 3^2 + 3^0 = 10
    k_cool(10, 42) == 101010
    k_cool(128, 5000) == 9826529652304384 # The actual result is larger than 10^16 + 61,
                                          # so k_cool returns the remainder of division by 10^16 + 61
    """

    """
    Approach: Given n, we can check the bits that are on - these correspond to
    powers of k we'd like to sum. To keep our arithmetic fast, we can keep
    taking mods throughout our operation, as the output will be invariant.
    This ensures the integers being manipulated stay small, or our operations
    will stop taking constant time (and will scale with the number of bits
    each integer is being represented by).
    Runs in O(log n) for the given n
    """
 
    MODULUS = 10**16 + 61

    k %= MODULUS

    k_pow = 1

    ans = 0
    while n > 0:
        if n & 1 == 1:
            ans += k_pow
            ans %= MODULUS
        n >>= 1
        k_pow *= k
        k_pow %= MODULUS

    return ans


def number_game(numbers: list[int]) -> tuple[str, int]:
    """
    @numbers@ is an unordered array of integers. The array is guaranteed to be of even length.
    Return a tuple consisting of the winner's name and the winner's score assuming that both play optimally.
    "Optimally" means that each player makes moves that maximise their chance of winning
    and minimise opponent's chance of winning.
    You are ALLOWED to use a tuple in your return here, like: return (x, y)
    Possible string values are "Alice", "Bob", and "Tie"

    Limitations:
        "It works":
            @numbers@ may contain up to 10'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^6
        "Exhaustive":
            @numbers@ may contain up to 100'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16
        "Welcome to COMP3506":
            @numbers@ may contain up to 300'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16

    Examples:
    number_game([5, 2, 7, 3]) == ("Bob", 5)
    number_game([3, 2, 1, 0]) == ("Tie", 0)
    number_game([2, 2, 2, 2]) == ("Alice", 4)

    For the second example, if Alice picks 2 to increase her score, Bob will pick 3 and win. Alice does not want that.
    The same happens if she picks 1 or 0, but this time she won't even increase her score.
    The only scenario when Bob does not win immediately is if Alice picks 3.
    Then, Bob faces the same choice:
    pick 1 to increase his score knowing that Alice will pick 2 and win, or pick 2 himself.
    The same happens on the next move.
    So, nobody picks any numbers to increase their score, which results in a Tie with both players having scores of 0.
    """

    """
    #Pythonic approach with in-builts
    
    numbers.sort(reverse=True)
    alice = 0
    bob = 0
    for i, e in enumerate(numbers):
        if i % 2 == 0:
            if e % 2 == 0:
                alice += e
        else:
            if e % 2 == 1:
                bob += e

    if alice > bob:
        return "Alice", alice
    if alice < bob:
        return "Bob", bob
    return "Tie", alice
    """

    """
    Approach: Since the optimal move for either Alice or Bob is to take the
    highest value no matter whether it contributes to their own score or not,
    we can simply sort the list and then iterate it high to low.
    Time: O(n log n) expected (since we use quicksort).
    """
    my_list = DynamicArray()
    my_list.build_from_list(numbers)
    my_list.sort()
    my_list.reverse()
    alice = 0
    bob = 0
    index = 0
    for element in my_list.iterate():
        # Alice's turn
        if index % 2 == 0:
            # Alice gains points
            if element % 2 == 0:
                alice += element
            # Or Alice 'steals' but does not gain
        else:
            # Bob gains points
            if element % 2 == 1:
                bob += element
            # Or Bob 'steals' but does not gain
    if alice > bob:
        return "Alice", alice
    if alice < bob:
        return "Bob", bob
    return "Tie", tie

def road_illumination(road_length: int, poles: list[int]) -> float:
    """
    @poles@ is an unordered array of integers.
    Return a single floating point number representing the smallest possible radius of illumination
    required to illuminate the whole road.
    Floating point numbers have limited precision. Your answer will be accepted
    if the relative or absolute error does not exceed 10^(-6),
    i.e. |your_ans - true_ans| <= 0.000001 OR |your_ans - true_ans|/true_ans <= 0.000001

    Limitations:
        "It works":
            @poles@ may contain up to 10'000 elements.
            0 <= @road_length@ <= 10^6
            Each element is in range 0 <= poles[i] <= 10^6
        "Exhaustive":
            @poles@ may contain up to 100'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16
        "Welcome to COMP3506":
            @poles@ may contain up to 300'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16

    Examples:
    road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) == 2.5
    road_illumination(5, [2, 5]) == 2.0
    """

    """
    # Another pythonic one for you - see how much functionality we take
    # for granted!
    poles.sort()
    d = poles[0]
    d = max(d, road_length - poles[-1])
    for i in range(1, len(poles)):
        d = max(d, (poles[i] - poles[i - 1]) / 2)
    return d
    """
    
    """
    Approach: Once again, this problem relies on sorting. If we sort the
    poles, we can make a linear pass to find the largest pole-to-pole delta -
    plus a little extra work to check the start and end of the road.
    Runs in O(n log n) expected.
    """
    
    # We never tested this case, but it does exist...
    if len(poles) == 0:
        return float('inf')

    my_list = DynamicArray()
    my_list.build_from_list(poles)
    my_list.sort()

    # First, let us check road_start <-> first_pole
    max_dist = my_list[0]

    # Then, we check last_pole <-> road_end
    end_dist = road_length - my_list[my_list.size() - 1]
    if end_dist > max_dist:
        max_dist = end_dist

    # Finally, check all pole-to-pole deltas
    for i in range(1, my_list.size()):
        this_dist = (poles[i] - poles[i-1]) / 2
        if this_dist > max_dist:
            max_dist = this_dist
    return max_dist
