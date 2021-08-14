'''
 write a function that takes in an array of edges for an undirected graph and two nodes.
 Return a boolean indicating whether or not there exists a path between nodes
'''

from collections import defaultdict
class Solution:
    def hasPath(self,edges,source,target):
        graph=self.buildgraph(edges)

        def dfs(source,visited):
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


    def buildgraph(self,edges):
        graph=defaultdict(list)

        for edge in edges:
            a,b=edge
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