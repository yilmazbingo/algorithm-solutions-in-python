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
                    stack = deque()
                    stack.append([row, col])
                    grid[row][col] = 0
                    while len(stack):
                        current = stack.popleft()
                        res.append(current)
                        current_row = current[0]
                        current_col = current[1]
                        for direction in self._directions:
                            new_row = current_row + direction[0]
                            new_col = current_col + direction[1]
                            if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                                continue
                            if grid[new_row][new_col] == 1:
                                stack.append([new_row, new_col])
                                grid[new_row][new_col] = 0
                    if all(grid1[coordinate[0]][coordinate[1]] == 1 for coordinate in res):
                        count += 1
        return count

grid1=[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2=[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
s=Solution()
print(s.countSubIslands(grid1,grid2)) #3