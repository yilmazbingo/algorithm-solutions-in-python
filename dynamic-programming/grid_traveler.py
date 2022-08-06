# https://leetcode.com/problems/unique-paths/
# m x n grid are given.  You can move either to right or down
# same logic as fibonacci
# hpw many different times can u walk down to the right end


class Solution:
    def uniquePaths(self, a: int, b: int,memo={}) -> int:
        key=str(a)+','+str(b)
        # memoizing how many ways we can reach the target from each coordinate
        if key in memo:
            return memo[key]
        # this means grid is empty, it is invalid. we write this because we might hit this when we a-1 or b-1
        if a==0 or b==0:
            return 0
        if a==1 or b==1:
            return 1
        # If I go down one down, I am reducing number of rows, I am going right, I am reducing number of columns by 1
        memo[key]=self.uniquePaths(a-1,b,memo)+self.uniquePaths(a,b-1,memo)
        return memo[key]

s=Solution()
print(s.memo(3,3))