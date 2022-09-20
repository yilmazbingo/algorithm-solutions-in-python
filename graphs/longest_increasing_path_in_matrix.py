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

            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1
            for dx, dy in dirs:
                r, c = i + dx, j + dy
                if not invalid(r, c) and matrix[r][c] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(r, c))

            return dp[i][j]

        c = 0
        for i in range(rows):
            for j in range(cols):
                c = max(c, dfs(i, j))

        return c