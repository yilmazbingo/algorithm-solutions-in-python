'''
146.Medium LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
    - `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''
# it is called LRU because our size is limited and we remove the Least Recently Used item
# The functions get and put must each run in O(1) average time complexity. That is why we use hashmap and deque
from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()
    # Look up for hash map is O(1)
    def get(self, key: int) -> int:
        if key in self.m:
            value=self.m[key]
            # if the key already exists remove and update it
            self.deq.remove(key)
            self.deg.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            if self.c==len(self.deq):
                oldest=self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)
        self.m[key]=value
        self.deq.append(key)

# . Python’s collections module provides a class called deque that’s specially designed to provide fast and memory-efficient ways to append and pop item
# from both ends of the underlying data structure.