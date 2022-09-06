# Given a DIRECTED graph, design an algorithm to find out whether there is a route between two nodes s and t.
# https://www.lintcode.com/problem/176/

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    # since this is directed it does not have visited
    # all  edges can be traversed in a single direction
    def hasRoute(self, graph, s, t):
        if s==t:
            return True
        for neighbor in s.neighbors:
            if self.hasRoute(graph,neighbor,t):
                return True
        return False



    def bfs(self, graph, s, t):
        queue = deque()
        queue.append(s)
        while len(queue):
            current = queue.popleft()
            if current == t:
                return True
            for neighbor in current.neighbors:
                queue.append(neighbor)
        return False

