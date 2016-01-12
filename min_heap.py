from typing import Optional, Any, Sequence
from math import floor


class HeapUnderflowError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


class MinHeap:
    def __init__(self, items: Sequence[int]):
        self.heap_size = len(items)
        self.heap = items
        for i in range(floor(self.heap_size/2.0), 0, -1):
            self.min_heapify(i-1)
    
    def min_heapify(self, i):
        # Create (index, value) tuples for each node
        lefti = self.__left(i)
        righti = self.__right(i)
        left = (lefti, self.__get(lefti))
        right = (righti, self.__get(righti))
        parent = (i, self.__get(i))
        
        smallest = min(left, right, parent,
                       key=lambda n: n[1] if n[1] else float('inf'))

        if smallest[1] != parent[1]:
            self.__set(parent[0], smallest[1])
            self.__set(smallest[0], parent[1])
            self.min_heapify(smallest[0])

    def get_min(self):
        return self.__get(0)

    def pop_min(self):
        if self.heap_size < 1:
            raise HeapUnderflowError('No items left in heap.')
        min = self.get_min()
        self.__set(1, self.__get(self.heap_size-1))
        self.heap_size -= 1
        self.min_heapify(1)
        return min

    def decrease_key(self, i, key):
        if key > self.__get(i):
            raise ValueError('Key is larger than existing key.')
        self.__set(i, key)
        while i > 0 and self.__get(self.__parent(i)) > self.__get(i):
            parenti = self.__parent(i)
            temp = self.__get(i)
            self.__set(i, self.__get(parenti))
            self.__set(parenti, temp)
            i = parenti

    def insert(self, key):
        self.heap_size += 1
        self.__set(self.heap_size-1, key)
        self.decrease_key(self.heap_size-1, key)

    def __get(self, i):
        return self.heap[i] if len(self.heap) > i else None

    def __set(self, i, value):
        if i < len(self.heap):
            self.heap[i] = value
        else:
            self.heap.append(value)

    def __left(self, index: int):
        return 2*(index+1) - 1

    def __right(self, index: int):
        return 2*(index+1)

    def __parent(self, index: int):
        return int(floor((index+1)/2.0)) - 1

    def __str__(self):
        return str(self.heap)

h = MinHeap([16,14,10,8,7,9,3,2,4,1])
h.decrease_key(4, 3)