'''
743. Network Delay Time- Medium

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''

from collections import defaultdict
import heapq
from typing import List

# Dijkstra algorithm is BFS, it uses minimum heap, aka priority-Queue
# in each layer, neighbor nodes will be added to minHeap. minHeap gets us the min value in Log(N)
# In meanHeap we keep (Path,Node). initially (0,1). it costs 0 to reach node 1
# E=V^2. edges can be bidirectinal. so for each edge we could push V^2 nodes to minHeap. finding min is Log(V^2)
# we do this operation E times. so T: 2 * E(Log(V))
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        edges = defaultdict(list)
        for u, v, cost in times:
            edges[u].append((v, cost))
        # min_heap sorts by time. we alwyats pop the lowest time
        min_heap = [(0, k)]
        # we dont wanna go in cycle. in loop
        visit = set()
        t = 0
        while min_heap:
            cost1, node1 = heapq.heappop(min_heap)
            print(cost1)
            if node1 in visit:
                continue
            visit.add(node1)
            t = max(t, cost1)
            for neighbor, cost2 in edges[node1]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, (cost1 + cost2, neighbor))
        return t if len(visit) == n else -1


t = [
    [1, 2, 9],
    [1, 4, 2],
    [2, 5, 1],
    [4, 2, 4],
    [4, 5, 6],
    [3, 2, 3],
    [5, 3, 7],
    [3, 1, 5],
];
s = Solution()

s.networkDelayTime(t, 5, 1)