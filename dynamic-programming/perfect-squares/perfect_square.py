'''Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.'''
# similar to coin change
# 12=4+4+4


class Solution:
    # botom up aproach, big problem n depends on the smaller subproblems. base case is n=0
    # T =O(n * log(N))
    def numSquares(self,n:int)->int:
        # as we go, we calculate what is the minimum number of perfect squares does it take for us to get target
        dp=[n]*(n+1)
        dp[0]=0
        for target in range(1,n+1):
            for s in range(1,target+1):
                square=s*s
                if target-square<0:
                    break
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]



