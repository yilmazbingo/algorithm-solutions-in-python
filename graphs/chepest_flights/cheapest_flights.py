'''
787. Medium Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
from typing import List
from collections import defaultdict
import heapq
# If I go from 0 -> 1 -> 3 that means I make only one stop at 1
# we cannot use the Djikastra because we are given condition "with at most k stops"
# IN bellman-ford I make n-1 bfs searches. i relex them n-1 times
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # defaultdict(<class 'dict'>, {0: {1: 100}, 1: {2: 100, 3: 600}, 2: {0: 100, 3: 200}})
        graph = defaultdict(dict)
        for source, dest, w in flights:
            graph[source][dest] = w
        # we have to run k+1 times
        min_heap = [(0, src, k+1)]
        # visited[x] record the remaining steps to reach x with the lowest cost.
        # in djikastra, when visit a node we dont visit again, because when you popped out of heap, we already found the best distance
        # we might prefer to get to a node with the longer distance but fewer stop
        visited = [0] * n
        while min_heap:
            current_cost, current_node, current_k = heapq.heappop(min_heap)
            if current_node == dst:
                return current_cost
            # visited[x] record the remaining steps to reach x with the lowest cost.
            # If visited[x] >= current_k, then no need to visit that case
            #  If it consumes more step, then we can discard it (because it already has a high cost).
            if visited[current_node] >= current_k:
                continue
            visited[current_node] = current_k
            # The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
            for neighbor, neighbor_cost in graph[current_node].items():
                heapq.heappush(min_heap, (current_cost+neighbor_cost, neighbor, current_k-1))
        return -1