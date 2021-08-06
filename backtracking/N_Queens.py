

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
