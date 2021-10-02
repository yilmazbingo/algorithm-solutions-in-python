'''
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''
# queeen can move all 4 directions and diagonally.
# each queen has to be in different column, row and diagonal
# pattern for negative diagonal. we are increasing row and col values by 1. r-c stays constant
# pattern for positive diagonal. r+c stays constant
from typing import List
class Solution:
    def solve(self,n:int)->List[List[int]]:
        res=[]
        col=set()
        posDiag=set()
        negDiag=set()
        board=[["."]*n for _ in range(n)]

        def dfs(r:int):
            if r==n:
                copied_board=["".join(row) for row in board ]
                res.append(copied_board)
                return
            for c in range(n):
                if c in col or c+r in posDiag or r-c in negDiag:
                    continue
                board[r][c]="Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                dfs(r+1)

                board[r][c]="."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        dfs(0)

        return res
