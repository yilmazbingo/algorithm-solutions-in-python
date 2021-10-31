'''
787. Medium Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
# k=0 is the direct flight
from typing import List
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list=[[] for _ in range(n)]
        # min cost that will get me to the city
        output=[float("inf") for _ in range(n)]
        output[src]=0
        for u,v,weight in flights:
            adj_list[u].append((v,weight))

        queue=deque()
        # -1 number of stops we made so far
        queue.append((src,-1,0))
        while queue:
            source,stop,cost=queue.popleft()
            if stop>=k:
                break
            # we have to track the cost so far. that makes it dynamic programming
            for v,w in adj_list[source]:
                if cost+w<output[v]:
                    output[v]=cost+w
                    queue.append((v,stop+1,cost+w))

        if output[dst]==float('inf'):
            return -1
        else:
            return output[dst]
