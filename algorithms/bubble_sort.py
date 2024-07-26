import random


def bubble_sort(input):
    for i in range(len(input) - 1):
        for j in range(len(input) - 1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)
    bubble_sort(arr)
    assert sorted_arr == arr
