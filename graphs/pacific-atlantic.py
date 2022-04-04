from typing import List

class Solution:
    # T:O(N*M) because we start from pacific edge and check if recahes atlantic. that way we do not revisit nodes again
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # all the positions thate can reach pac and atl
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # we are going from ocean to all the cells
            # prevHeight should be less or equal to the height
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            # if we are not returning means we found a new cell
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
       # this is the first row and last row
        for c in range(COLS):
            # with prevHeight I check if I am allowed to visit that cell
            dfs(0, c, pac, heights[0][c])
            # this is the last row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        # this is the first col and last row
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][c])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

