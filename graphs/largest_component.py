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
    def largest(self,graph):
        visited=set()
        longest=0
        # always decide what recursive function will return
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            # this is the size of the current node
            size=1
            for neighbor in graph[node]:
                size+=dfs(neighbor)
            return size
        # explore all the neightbors of nodes. I need to calculate length of all possible components
        for node in graph:
            longest=max(dfs(node),longest)
        return longest

s=Solution()
print(s.largest(adj_list))