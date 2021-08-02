# since we can move only up or right, there is only one way to reach all elements in first row and first column.
# the number of ways to reach i'th position is the sum of number of ways we can reach cell above it and on its left

class Solution:
    def travel(self,m,n):
        dp=[[0 for x in range(m)] for y in range(n)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

s=Solution()
print(s.travel(3,3))