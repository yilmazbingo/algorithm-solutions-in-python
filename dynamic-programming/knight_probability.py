"""
On a given nxn chessboard, a knight piece will start at the r-th row and c-th column. The knight will attempst to make k moves.
A knight can be move in 8 possible ways. Each move will choose one of these 8 at random. The knight continues
moving until it finishes k moves or it moves off the chessboard.
Return the porbability that the knight is on the chessboard after it finishes its moving.

A knight can move in shape of L.
"""

# knight has a cetain probability based on where on the chessboard
class Solution:
    def __init__(self):
        self.directions=[
                          [-2, -1],[-2, 1], [-1, 2],[1, 2], [2, 1],[2, -1],[1, -2],[-1, -2],
                        ]
    def memoized(self,size,moves,col,row):
        def dfs(size,moves,col,row,memo={}):
            key=str(moves) + "," + str(row) + "," + str(col)
            res=0
            if key in memo:
                return memo[key]
            if row<0 or row>=size or col<0 or col>=size:
                return 0
            if moves==0:
                return 1
            for dir in self.directions:
                res += dfs(size, moves - 1, col + dir[1], row + dir[0]) / 8
            memo[key]=res
            return memo[key]
        return dfs(size,moves,col,row)


    ## I HAVE TO WORK ON THIS
    def tabulation(self,size,moves,col,row):
        dp=[ [[0 for i in range(moves)]  for x in range(size+1)] for y in range(size+1)]
        print(dp)
        # this is starting point.
        dp[0][row][col]=1
        for move in range(1,moves+1):
            for r in range(row):
                for c in range(col):
                    for dir in self.directions:
                        prev_row=r+dir[0]
                        prev_col=c+dir[1]
                        if c<=size and c>0 and r>0 and r<=size:
                            dp[move][r][c]+=dp[move-1][prev_row][prev_col]/8
        res=0
        for i in range(size):
            for j in range(size):
                res+=dp[moves][i][j]
        return res



s=Solution()
print(s.unoptimized(3,2,0,0))
print(s.memoized(3,2,0,0))
print(s.tabulation(3,2,0,0))


