'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
785. Medium Is Graph Bipartite?
'''
# a bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V.
from typing import List
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        # ALWAYS WHEN WORKING UNDIRECTED GRAPH, MAKE SURE YOU DO NOT REVISIT
        colors = [-1] * N
        # in case it is unconnected, make sure i touch each vertex
        for i in range(N):
            # means we already visited, we do not visit again
            if colors[i] != -1:
                continue
            queue = deque()
            #  each node is numbered between 0 and n - 1. that is why we are adding "i"
            queue.append((i, 0))
            while queue:
                node, color = queue.popleft()
                # this means untouched. so update the colors list
                if colors[node] == -1:
                    colors[node] = color
                    for neighbor in graph[node]:
                        # neighbors should be different color. ^ is XOR
                        queue.append((neighbor, color ^ 1))
                # incase somethingelse changed it. this might be cuase by other unccnnected part
                if colors[node] != color:
                    return False
        return True
