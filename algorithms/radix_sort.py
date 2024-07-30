import random


# adjusting counting sort for bigger numbers
def radix_sort(input):
    def counting_sort(arr, digit):
        # ... 3rd 2nd 1st 0th
        original = list(arr)
        for i in range(len(arr)):
            if len(str(arr[i])) > digit:
                arr[i] = int((str(arr[i])[::-1])[digit])
            else:
                arr[i] = 0
        print(f"Radix array = {arr}")
        count_arr = [0] * (max(arr) + 1)
        sorted_arr = [None] * len(arr)

        for num in arr:
            count_arr[num] += 1

        for i in range(1, len(count_arr) - 1):
            count_arr[i] += count_arr[i - 1]

        for i in reversed(range(1, len(count_arr))):
            count_arr[i] = count_arr[i - 1]

        count_arr[0] = 0
        print(f"Original = {original}")
        for original_num, num in zip(original, arr):
            sorted_index = count_arr[num]
            count_arr[num] += 1
            sorted_arr[sorted_index] = original_num

        return sorted_arr

    max_digits = len(str(max(input)))
    sorted_arr = input
    for i in range(max_digits):
        sorted_arr = counting_sort(sorted_arr, i)
    return sorted_arr


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)

    assert sorted_arr == radix_sort(arr)
