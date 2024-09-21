import random


def quick_sort(input):
    def partition(input, low, high):
        # we choose the element in the last index
        # as our pivot
        pivot = high
        # weak sort till the pivot
        index = low - 1
        for i in range(low, high):
            # we stack the elements smaller than the pivot
            # to the beginning of the array
            if input[i] <= input[pivot]:
                index += 1
                input[index], input[i] = input[i], input[index]
        # finally we put the index on the
        # 'top of the stack' of the numbers elements
        # smaller than it
        index += 1
        input[index], input[pivot] = input[pivot], input[index]
        # this automatically makes the elements larger than
        # the pivot being placed on the right side of the pivot
        return index
        # we return the position of the pivot

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
