'''Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.'''
# similar to coin change
# 12=4+4+4


class Solution:
    # botom up aproach, big problem n depends on the smaller subproblems. base case is n=0
    # T =O(n * log(N)) not o(n^2) becase we stop when n^2 is greater than n
    def numSquares(self,n:int)->int:
        # first check if sqrt of n is equal to n
        if n==0:
            return 0
        if n<=3:
            return n
        # as we go, we calculate what is the minimum number of perfect squares does it take for us to get target
        # for n=12, dp=[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3]
        dp=[n]*(n+1)
        dp[0]=0
        # first for loop to decide how many perfect squares are there for dp[target]
        for target in range(1,n+1):
            for s in range(1,target+1):
                square=s*s
                if target-square<0:
                    break
                # 1+dp[target-square] is number of squares that needed for the rest. +1 is for the number that is already calculated
                # 5=1*1 + 2*2
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]



