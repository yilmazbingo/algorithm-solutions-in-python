'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
float('inf - Infinity means an empty room.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with float('inf
'''
'''
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides 
an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
'''

from typing import List
from collections import deque
directions = [[-1, 0], [0, 1], [1, 0], [0, -1] ]
class Solution:
    def depthFirst(self, rooms):
        ROWS, COLS = len(rooms), len(rooms[0])

        def backtrack(r, c, count):
            if r < 0 or r == ROWS or c < 0 or c == COLS or rooms[r][c] == -1 or count > rooms[r][c]:
                return
            rooms[r][c] = count
            for dir in directions:
                backtrack(r + dir[0], c + dir[1], count + 1);

        for r in range(ROWS):
            for c in range(COLS):
                # find all the gates
                if rooms[r][c] == 0:
                    backtrack(r, c, 0)
        print(rooms)

    def breadthFirst(self,rooms:List[List[int]])->None:
        ROWS,COLS=len(rooms),len(rooms[0])
        visit=set()
        q=deque()

        def addRoom(r,c):
            #                                     (r,c in visit) this is was causing error
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or rooms[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                # find all the gates
                if rooms[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        dist=0
        while q:
            for i in range(len(q)):
                # popping out the gates
                r,c=q.popleft()
                # change the gate for being the current distance
                # after first layer I will be adding the distances of 1 because i increase dist++

                rooms[r][c] = dist
                # add all the aadjacent rooms to the ques
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist+=1
        print(rooms)
test = [
  [float('inf'), -1, 0, float('inf')],
  [float('inf'), float('inf'), float('inf'), 0],
  [float('inf'), -1, float('inf'), -1],
  [0, -1, float('inf'), float('inf')]
];

s=Solution()
s.breadthFirst(test)
s.depthFirst(test)