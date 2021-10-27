'''
210.Medium  Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

from collections import deque
from typing import List

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * n
        adj_list = [[] for _ in range(n)]
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        stack = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        count = 0
        # res=[] would not make difference
        res = deque()
        while stack:
            current = stack.popleft()
            res.append(current)
            count += 1
            adjacent = adj_list[current]
            for i in range(len(adjacent)):
                adj = adjacent[i]
                indegree[adj] -= 1
                if (indegree[adj] == 0):
                    stack.append(adj)
        return res if count == n else []
