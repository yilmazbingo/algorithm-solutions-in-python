"""
797. Medium All Paths From Source to Target
Given a DIRECTED acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
# https://www.lintcode.com/problem/1020/

# Time:  O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# Space: O(n)
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        def dfs(cur,path):
            if cur==len(graph)-1:
                res.append(path.copy())
                return
            for node in graph[cur]:
                dfs(node,path+[node])
        dfs(0,[0])
        return res

s=Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))