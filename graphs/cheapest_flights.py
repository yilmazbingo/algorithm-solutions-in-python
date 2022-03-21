'''
787. Medium Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, dest, w in flights:
            graph[source][dest] = w
        min_heap = [(0, src, k+1)]
        # visited[x] record the remaining steps to reach x with the lowest cost.
        visited = [0] * n
        while min_heap:
            w, current_node, current_k = heapq.heappop(min_heap)
            if current_node == dst:
                return w
            # If visited[x] >= current_k, then no need to visit that case
            if visited[current_node] >= current_k:
                continue
            visited[current_node] = current_k
            for y, dw in graph[current_node].items():
                heapq.heappush(min_heap, (w+dw, y, current_k-1))
        return -1