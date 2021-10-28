# takes an adjacency list of an undirected graph and return the number of connected components within the graph

adj_list = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2],
};

class Solution:
    def count_connected(self,graph):
        visited=set()
        count=0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            # If I get here that means i explored all
            return True
        # explore all the neightbors of nodes
        for node in graph:
            if dfs(node):
                count+=1
        return count

s=Solution()
print(s.count_connected(adj_list))