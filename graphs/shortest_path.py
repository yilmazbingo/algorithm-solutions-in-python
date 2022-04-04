# given a 2D array find the shortest path to the destination
# distance is number of edges between nodes

edges = [
  ["w", "x"],
  ["x", "y"],
  ["z", "y"],
  ["z", "v"],
  ["w", "v"],
]
# T:O(N)
# dfs forces me look in one direction as fas as possible, until I have to switch directions
# dfs might search in totally wrong direction
from collections import defaultdict, deque
class Solution:
    def bfs(self,edges,source,target):
        graph=self.buildGraph(edges)
        visited=set()
        queue=deque()
        queue.append([source,0])
        visited.add(source)
        while len(queue):
            node,distance=queue.popleft()
            if node == target:
                return distance
            # notice that I did not add it to the set here
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor,distance+1])
        return -1

    def buildGraph(self,edges):
        graph=defaultdict(list)
        for edge in edges:
            node1,node2=edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        print(graph)
        return graph

s=Solution()
print(s.bfs(edges,"w","z")) #2