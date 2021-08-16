'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''
# Leetcode 1584
import heapq

'''
- We want to connect all nodes without creating cycle. This is called Minimum Spanning Algorithm. we need (n-1) edges
- Prim's algorithm solves this with the minimum cost of the edges

'''
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj_list={i:[] for i in range(n)}
        # Creating the adjacenc list
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                distance=abs(x1-x2)+abs(y1-y2)
                adj_list[i].append([distance,j])
                adj_list[j].append([distance,i])
        res=0
        visited=set()
        min_heap=[[0,0]]
        while len(visited)<n:
            cost,node=heapq.heappop(min_heap)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            # checking node's neighbor
            for cost,neighbor in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap,[cost,neighbor])
        return res


