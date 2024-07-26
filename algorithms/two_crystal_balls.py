# Given two crystal balls that will break if dropped from high enough
# distance, determine the exact spot in which it will break in the
# most optimized way
from math import sqrt


def find_the_spot(input):
    # two crystal balls = we have two go's
    # use the first ball to jump sqrt(n) steps
    # use the second ball to linearly search the correct spot
    curr_index = 0
    break_index = None
    last_index = None
    while curr_index < len(input):
        if input[curr_index]:
            break_index = curr_index
            break
        last_index = curr_index
        curr_index += int(sqrt(len(input)))
    for index in range(last_index, break_index):
        if input[index]:
            print(f"The spot is index: {index}")
            return index


def test_():
    test_arr = [
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
    ]

    assert find_the_spot(test_arr) == 5
