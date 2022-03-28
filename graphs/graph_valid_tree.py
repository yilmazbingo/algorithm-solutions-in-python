# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
'''
A tree is a special undirected graph. It satisfies two properties
- It is connected
- It has no cycle.
'''
from collections import defaultdict
from typing import List
# no cycle can be expressed as # of nodes == # of edges + 1.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        visited = set()
        def dfs(root):
            visited.add(root)
            for node in graph[root]:
                if node in visited:
                    continue
                dfs(node)
        dfs(0)
        return len(visited) == n and len(edges) == n - 1