'''
1905. Medium Count Sub Islands
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).
An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
'''

from typing import List
from collections import deque
class Solution:
    def __init__(self):
        self._directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def countSubIslands(self, grid1: List[List[int]], grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                res = []
                if grid[row][col] == 1:
                    queue = deque()
                    queue.append([row, col])
                    # this will make sure i do not revisit again
                    grid[row][col] = 0
                    while len(queue):
                        current = queue.popleft()
                        res.append(current)
                        current_row = current[0]
                        current_col = current[1]
                        for direction in self._directions:
                            new_row = current_row + direction[0]
                            new_col = current_col + direction[1]
                            if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                                continue
                            if grid[new_row][new_col] == 1:
                                queue.append([new_row, new_col])
                                # I make it 0 cause, next [row][coord] will be zero and if grid[row][col] == 1 wont meet
                                grid[new_row][new_col] = 0
                    if all(grid1[coordinate[0]][coordinate[1]] == 1 for coordinate in res):
                        count += 1
        return count

grid1=[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2=[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
s=Solution()
print(s.countSubIslands(grid1,grid2)) #3