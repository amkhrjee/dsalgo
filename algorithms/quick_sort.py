import random


def quick_sort(input):
    def partition(input, low, high):
        pivot = high
        # weak sort till the pivot
        index = low - 1
        for i in range(low, high):
            if input[i] <= input[pivot]:
                index += 1
                input[index], input[i] = input[i], input[index]
        index += 1
        input[index], input[pivot] = input[pivot], input[index]
        return index

    def sort(input, low, high):
        if low >= high:
            return
        pivot = partition(input, low, high)
        sort(input, low, pivot - 1)
        sort(input, pivot + 1, high)

    sort(input, 0, len(input) - 1)


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)
    quick_sort(arr)
    assert sorted_arr == arr
