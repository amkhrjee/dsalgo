import random


# Inspired by Jon Bentley's pseudocode in Programming Pearls
# https://books.google.co.in/books?id=kse_7qbWbjsC&pg=PA116&redir_esc=y#v=onepage&q&f=false
def insertion_sort(input):
    # loop over the entire array
    for i in range(len(input)):
        # go backwards from the current position
        for j in range(i, 0, -1):
            if input[j - 1] > input[j]:
                input[j - 1], input[j] = input[j], input[j - 1]


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)
    insertion_sort(arr)
    assert sorted_arr == arr
