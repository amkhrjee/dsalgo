# We build heap from array

import random


class MaxHeap:
    def __init__(self, arr):
        # heap index starts at 1 for convenience
        self.heap = [None] + arr
        self._build_heap(self.heap)

    def _build_heap(self, heap):
        heap_size = len(heap)
        for i in range(heap_size // 2, 0, -1):
            self._max_heapify(heap, heap_size, i)

    def _max_heapify(self, heap, heap_size, index):
        def left(i):
            return 2 * i

        def right(i):
            return 2 * i + 1

        left_child = left(index)
        right_child = right(index)

        # The root should be the largest
        largest = index
        if left_child < heap_size and heap[left_child] > heap[largest]:
            largest = left_child

        if right_child < heap_size and heap[right_child] > heap[largest]:
            largest = right_child

        if largest != index:
            # the item at the root is not largest,
            # swap it with whatever _is_ the largest
            heap[largest], heap[index] = heap[index], heap[largest]
            self._max_heapify(heap, heap_size, largest)

    def pop(self):
        val = self.heap.pop(1)
        self._build_heap(self.heap)
        return val

    def peek(self):
        return self.heap[1]

    # Heap sort
    def sort(self):
        # returns the sorted array
        heap = self.heap
        for i in range(len(heap) - 1, 1, -1):
            heap[i], heap[1] = heap[1], heap[i]
            self._max_heapify(heap, i, 1)

        return heap[1:]


def test_():
    arr = [random.randint(0, 100) for _ in range(10)]
    max_heap = MaxHeap(arr)
    assert max_heap.pop() == max(arr)
    arr.remove(max(arr))
    assert max_heap.peek() == max(arr)
    assert sorted(arr) == max_heap.sort()
