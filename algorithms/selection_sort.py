import random


def selection_sort(input):
    for i in range(len(input)):
        min_index = i
        for j in range(i + 1, len(input)):
            if input[min_index] < input[j]:
                min_index = j
        input[min_index], input[i] = input[i], input[min_index]


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)
    selection_sort(arr)
    assert sorted_arr == arr
