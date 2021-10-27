'''
787. Medium Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices.copy()
            for source, dest, price in flights:
                # we have only 2 conditions check for
                # first if price to reach source is inf, that means we cannot reach this src
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < temp_prices[dest]:
                    temp_prices[dest] = prices[source] + price
            prices = temp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]