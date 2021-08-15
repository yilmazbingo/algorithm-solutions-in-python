# given a 2D array find the shortest path to the destination
# Use bfs

edges = [
  ["w", "x"],
  ["x", "y"],
  ["z", "y"],
  ["z", "v"],
  ["w", "v"],
]


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