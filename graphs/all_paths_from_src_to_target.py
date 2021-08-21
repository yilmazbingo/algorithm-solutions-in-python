"""
Given a DIRECTED acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
# leetcode 797
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target=len(graph)-1
        def dfs(source,path,result):
            if source==target:
                result.append(path)
            for neighbor in graph[source]:
                print("path",path)
                dfs(neighbor,path+[neighbor],result)
        dfs(0,[0],result)
        return result

s=Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))