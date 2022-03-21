'''
 write a function that takes in an array of edges for an undirected graph and two nodes.
 Return a boolean indicating whether or not there exists a path between nodes
'''
# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/

# n=nodes, e=edges , O:T(e), O:S(n)
from collections import defaultdict
class Solution:
    def hasPath(self,edges,source,target):
        graph=self.buildgraph(edges)
        def dfs(source,visited):
            # in dfs, we isolate each node from entire graph
            if source in visited:
                return False
            visited.add(source)
            if source==target:
                return True
            for neighbor in graph[source]:
                if dfs(neighbor,visited):
                    return True
            return False
        return dfs(source,set())

    # edges represents connection between 2 nodes.  edges = [[0,1],[1,2],[2,0]],
    def buildgraph(self,edges):
        graph=defaultdict(list)
        for edge in edges:
            a,b=edge
            # this is undirected graph
            graph[a].append(b)
            graph[b].append(a)
        return graph

edges = [
  ["i", "j"],
  ["k", "i"],
  ["m", "k"],
  ["k", "l"],
  ["o", "n"],
]

s=Solution()
print(s.hasPath(edges,'j','m'))
print(s.buildgraph(edges))