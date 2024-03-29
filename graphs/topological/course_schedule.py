'''
207. Medium Course Schedule
There are a total of numCourses courses you have to take, LABELLED from 0 to numCourses - 1. You are given an array prerequisites where
 prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
#prereq:[[1,0],[2,3],[3,4]]
# We cannot finish courses if we have some kind of cycle. if 3->4 and 4->3
#if oyu hear there is some type of relationship between pairs of somehing inside of a question, it is most likely they are defining the relationship between two vertices
# because that relationship is dictated as an edge.

from typing import List
from collections import deque
class Solution:
    # T: O(len(prerequisites)+n^2)
    def topological(self, n: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * n
        # adjacency list is the way how we represent the graph
        adj_list = [[] for _ in range(n)]
        # [1,2] 2 =>1 pre[0] has one indegree
        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])
        # check indegree array items if any of them are zero
        stack = []
        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            current = stack.pop()
            count += 1
            # I need to find the adj of vertices and reduce their indegree value by 1 because I removed the node, so one less node is coming into them
            # for example 4:[1,2]  reduce indegree of 1 and 2
            for neighbor in adj_list[current]:
                # since we are removing the current node from stack, its neighbors will be losing 1 incoming node
                indegree[neighbor] -= 1
                if (indegree[neighbor] == 0):
                    stack.append(neighbor)
        # if by the end we did not touch every vortex, processed its value and removed from graph, then we know that there must be a cycle
        return count == n
    def can_finish(self,num_courses:int,prerequisites:List[List[int]]):
        # map each course to prereq list
        pre_map={i:[] for i in range(num_courses) }
        for course,pre in prerequisites:
            pre_map[course].append(pre)
        visit_set=set()
        def dfs(crs):
            # first thing in recursive functions, always write the base case first
            if crs in visit_set:
                # that means I run into a loop
                return False
            if pre_map[crs]==[]:
                # this tells us that current course has no prerequisite
                return True
            visit_set.add(crs)
            # we are checking if each courses prerequisites can be finished
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            # we finished visiting
            visit_set.remove(crs)
            # in case this course is visited again, since we already returned True, run base case again
            pre_map[crs]=[]
            return True
        # if graph was not fully connected, we had to run this for each course
        # 1-->2, 3-->4 so check if course 1,2,3,4 can individually be finished
        for crs in range(num_courses):
            if not dfs(crs):
                return False
        return True
       #------------------- consider some edge cases -------------
    def bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < len(prerequisites):
            return False
        if len(prerequisites) == 0:
            return True
        #   adj_list = [[]  for _ in range(len(prerequisites))]  this is same
        adj_list = [[] * len(prerequisites) for _ in range(len(prerequisites))]
        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])
        print(adj_list)
        # we have to perform traversal on each single node. In case we have unconnected components
        for i in range(numCourses):
            queue = deque()
            seen = {}
            # [[], [0], [0], [1], [1, 3]]
            for j in range(len(adj_list[i])):
                queue.append(adj_list[i][j])
            while queue:
                current = queue.popleft()
                seen[current] = True
                # we have cycle. while we perform traversal, if we are back to a node that we have seen before, we have cycle
                # for example, for node 1:[1] 1 ->1
                if current == i:
                    return False
                adjacent = adj_list[current]
                print(len(adjacent))
                for a in range(len(adjacent)):
                    next = adjacent[a]
                    if next not in seen:
                        queue.append(next)
        return True
s=Solution()
print(s.can_finish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]])) ## true
print(s.topological(2,[[0,1]])) # True