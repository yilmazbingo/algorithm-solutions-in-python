# it is called LRU because our size is limited anc we remove the Least Recently Used item
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

