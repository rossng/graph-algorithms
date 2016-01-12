from typing import Optional, Any, Sequence, TypeVar, Callable
from math import floor


class HeapUnderflowError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


T = TypeVar('T')


class MinHeap:
    def __init__(self, items: Sequence[T],
                 get_key: Callable[[T], int],
                 set_key: Callable[[T, int], None]):
        self.heap_size = len(items)
        self.heap = items
        self.get_key = get_key
        self.set_key = set_key
        for i in range(floor(self.heap_size / 2.0), 0, -1):
            self.min_heapify(i - 1)

    def min_heapify(self, i):
        # Create (index, key) tuples for each node
        lefti = self.__left(i)
        righti = self.__right(i)
        left = (lefti, self.__get(lefti))
        right = (righti, self.__get(righti))
        parent = (i, self.__get(i))

        smallest = min(left, right, parent,
                       key=lambda n: self.get_key(n[1]) if n[1] and self.get_key(n[1]) is not None else float('inf'))

        if self.get_key(smallest[1]) != self.get_key(parent[1]):
            self.__set(parent[0], smallest[1])
            self.__set(smallest[0], parent[1])
            self.min_heapify(smallest[0])

    def get_min(self):
        return self.__get(0)

    def pop_min(self):
        if self.heap_size < 1:
            raise HeapUnderflowError('No items left in heap.')
        min = self.get_min()
        self.__set(1, self.__get(self.heap_size - 1))
        self.heap_size -= 1
        self.min_heapify(1)
        return min

    def decrease_key(self, i, key):
        if key > self.get_key(self.__get(i)):
            raise ValueError('Key is larger than existing key.')
        self.set_key(self.__get(i), key)
        while i > 0 and self.__is_parent_larger(i):
            current = self.__get(i)
            parenti = self.__parent(i)
            parent = self.__get(parenti)
            self.__set(i, parent)
            self.__set(parenti, current)
            i = parenti

    def __is_parent_larger(self, i):
        return self.get_key(self.__get(self.__parent(i))) > \
               self.get_key(self.__get(i))

    def insert(self, item):
        self.heap_size += 1
        self.__set(self.heap_size-1, item)
        self.decrease_key(self.heap_size - 1, self.get_key(item))

    def __get(self, i):
        return self.heap[i] if len(self.heap) > i else None

    def __set(self, i, value):
        if i < len(self.heap):
            self.heap[i] = value
        else:
            self.heap.append(value)

    def __left(self, index: int):
        return 2 * (index + 1) - 1

    def __right(self, index: int):
        return 2 * (index + 1)

    def __parent(self, index: int):
        return int(floor((index + 1) / 2.0)) - 1

    def __str__(self):
        return str(self.heap)


def set_key(item, key):
    item[0] = key

#h = MinHeap([[16], [14], [10], [8], [7], [9], [3], [2], [4], [1]], lambda x: x[0], set_key)
#h.decrease_key(4, 3)
#h.insert([1])