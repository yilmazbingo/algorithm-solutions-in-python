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
# we go through every single edge when we traverse the graph and build adj list and and iterating over the graph
# T: O(E + V)
class Solution:
    def count_connected(self,graph):
        visited=set()
        count=0
        def dfs(node):
            # we start from the first node and explore it. then move to the next neighbor of the start point. since we already visited return False
            if node in visited:
                return False
            visited.add(node)
            # depending on api, for neighbor in node.neighbor
            for neighbor in graph[node]:
                # dfs's job is to add the node into the set
                dfs(neighbor)
            # When there is no more node left return True
            return True
        # explore all the neightbors of nodes. we use for loop if graph might have disconnected parts
        for node in graph:
            if dfs(node):
                count+=1
        return count

s=Solution()
print(s.count_connected(adj_list))