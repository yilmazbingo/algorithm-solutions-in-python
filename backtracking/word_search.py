# Given an m*n grid of characters board and string "Word" return true if word exists in the grid

from typing import List
class Solution:
    def exist(self,board:List[List[str]],word:str)->bool:
        ROWS,COLS=len(board),len(board[0])
        # we cannot revisit the same character twice
        path=set()
        # i is the current char in the word that we are looking for
        def dfs(r,c,i):
            # Base cases are passed to each dfs calls
            if i==len(word):
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            # res is boolean
            res=(dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                 dfs(r,c-1,i+1))
            # As we hand the result to the previos call, we also clean after ourself
            path.remove((r,c))
            # this is the final return
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False

    # T: O(n*m*dfs). what is the time complexity of the dfs
    # call stack of that dfs is always the len(word). 4^len(word)
    # we are calling dfs every single time for every position in the board
    # S: O(m * n)
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
