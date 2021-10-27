'''
785. Medium Is Graph Bipartite?
'''

from typing import List
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        colors = [-1] * N
        # in case it is unconnected, make sure i touch each vertex
        for i in range(N):
            # means we already visited, we do not visit again
            if colors[i] != -1:
                continue
            queue = deque()
            # we group 0 and 1
            queue.append((i, 0))
            while queue:
                node, color = queue.popleft()
                # this means untouched
                if colors[node] == -1:
                    colors[node] = color
                    for neighbor in graph[node]:
                        # neighbors should be different color
                        queue.append((neighbor, color ^ 1))
                if colors[node] != color:
                    return False
        return True
