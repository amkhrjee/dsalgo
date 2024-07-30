import random


def bucket_sort(input):
    buckets = [[] for _ in range(max(input))]
    for num in input:
        buckets[num - 1].append(num)
    sorted_array = []
    for bucket in buckets:
        for num in bucket:
            sorted_array.append(num)

    return sorted_array


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)

    assert sorted_arr == bucket_sort(arr)
