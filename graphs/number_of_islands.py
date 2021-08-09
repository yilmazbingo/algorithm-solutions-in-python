from typing import List
from collections import deque

# T:O(m*n) think logically. we touch only once each item
# bfs will happen only when we encounter 1's.
# S:O( max(m,n) because we always pop, stack's size will never be m*n
class Solution:
    def __init__(self):
        self._directions=[[1,0],[-1,0],[0,1],[0,-1]]

    def numIslands(self,grid:List[List[int]])->int:
            ROWS,COLS=len(grid),len(grid[0])
            count=0

            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col]=="1":
                        count+=1
                        stack=deque()
                        stack.append([row,col])
                        grid[row][col]="0"
                        while len(stack):
                            current=stack.popleft()
                            current_row=current[0]
                            current_col=current[1]
                            for direction in self._directions:
                                new_row=current_row+direction[0]
                                new_col=current_col+direction[1]
                                if new_row<0 or new_row>=ROWS or new_col<0 or new_col>=COLS:
                                    continue
                                if grid[new_row][new_col]=="1":
                                    stack.append([new_row,new_col])
                                    grid[new_row][new_col]="0"
            return count



