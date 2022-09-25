'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # what is the longest route i can take to reach [1][1] and i am doing that for every matrix index till i reach my destination.
        # By doing this if during recursion my dfs function reaches [1][1] again so it doesn't have to calculate the longest path for [1][1] again.
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        if rows <= 1 and cols <= 1:
            return 1
        def invalid(i, j):

            return i < 0 or j < 0 or i == rows or j == cols
        def dfs(i, j):
            # checks whether that index has already been calculated or not with the dp
            if dp[i][j] != -1:
                return dp[i][j]
            # if it is not calculated, run for loop
            dp[i][j] = 1
            for dir in dirs:
                r, c = i + dir[0], j + dir[1]
                if not invalid(r, c) and matrix[r][c] > matrix[i][j]:
                    # if next coord is greater add 1 and then call dfs
                    # all 4 neighbors will get a result. store the max one
                    dp[i][j] = max(dp[i][j], 1 + dfs(r, c))
            return dp[i][j]

        c = 0
        for i in range(rows):
            for j in range(cols):
                c = max(c, dfs(i, j))

        return c