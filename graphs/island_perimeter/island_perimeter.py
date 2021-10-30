'''
463-Easy
- You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

- Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).
- The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''
from typing import List
# perimeter means count the edges that touches the water
class Solution:
    def islandPerimeter(self,grid:List[List[int]])->int:
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        def dfs(r,c):
            if r<0 or r==ROWS or c==COLS or c<0 or grid[r][c]==0:
                # that means we are on the border. so we return 1
                return 1
            if (r,c) in visited:
                return 0
            # makes sure we call dfs for only 4 directions. not visit same direction
            visited.add((r,c))
            return dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return dfs(r,c)