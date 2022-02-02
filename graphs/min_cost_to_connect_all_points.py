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
- use manhattan distance as cost=[x1-x2]+[y1-y2]
'''
from typing import List
# T(n^2 log(N)) n^2 is the number of edges that we are gonna have, Log(N) will come from Prim's algorithm. Because we are using min_heap
class Solution:
    # points on x-y coordinate system
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj_list={i:[] for i in range(n)}
        # Creating the adjacenc list. edges are the cost of the each distance
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                distance=abs(x1-x2)+abs(y1-y2)
                adj_list[i].append([distance,j])
                adj_list[j].append([distance,i])
        res=0
        visited=set()
        # we can start from any single node. Then we are going to perform BFS on that node.
        # From here, all frontiers will be added to the min_heap. frontier mean other parts. for example if we connect to node2, node2 is a frontier
        # we add (cost,frontier) to the min_heap. because min_heap organize data based on the first_item. So when we pop out an item, we want to pop it out based on cost
        # to connect to first frontier, we are going to choose the min_cost frontier. then from that node we are going to look for its min_cost frontier
        min_heap=[[0,0]]
        # if we want to connect everything without creating cycle, it will take n-1 edges.
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


# since there are 5 points, each point will have 4 edges
points=[[0,0],[2,2],[3,10],[5,2],[7,0]]
s=Solution()
s.minCostConnectPoints(points)