import random


def merge_sort(input):
    def merge(left, right):
        sorted = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                sorted.append(left[left_idx])
                left_idx += 1
            else:
                sorted.append(right[right_idx])
                right_idx += 1
        while left_idx < len(left):
            sorted.append(left[left_idx])
            left_idx += 1
        while right_idx < len(right):
            sorted.append(right[right_idx])
            right_idx += 1
        return sorted

    def sort(input):
        if len(input) == 1:
            return input
        mid = len(input) // 2
        left = sort(input[:mid])
        right = sort(input[mid:])
        return merge(left, right)

    return sort(input)


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    sorted_arr = sorted(arr)
    m_sorted = merge_sort(arr)
    assert sorted_arr == m_sorted
