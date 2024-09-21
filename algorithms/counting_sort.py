import random


# works best for small range of numbers
# this is stable sort
def counting_sort(arr):
    count_arr = [0] * (max(arr) + 1)
    sorted_arr = [None] * len(arr)

    # populating the count array
    for num in arr:
        count_arr[num] += 1

    # cumulative sum towards right
    for i in range(1, len(count_arr) - 1):
        count_arr[i] += count_arr[i - 1]

    # right shift by 1
    for i in reversed(range(1, len(count_arr))):
        count_arr[i] = count_arr[i - 1]

    # 0th index is always 0
    count_arr[0] = 0

    # populating the sorted array
    for num in arr:
        sorted_index = count_arr[num]
        count_arr[num] += 1
        sorted_arr[sorted_index] = num

    return sorted_arr


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)

    assert sorted_arr == counting_sort(arr)
