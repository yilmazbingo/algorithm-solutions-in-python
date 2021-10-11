# m x n grid are given.  You can move either to right or down
# same logic as fibonacci
# hpw many different times can u walk down to the right end

class Solution:
    def travel(self,a,b):
        if a==0 or b==0:
            return 0
        if a==1 or b==1:
            return 1
        return self.travel(a-1,b) + self.travel(a,b-1)

    def memo(self,a,b,memo={}):
        key=str(a)+','+str(b)
        if key in memo:
            return memo[key]
        if a==0 or b==0:
            return 0
        if a==1 or b==1:
            return 1
        memo[key]=self.memo(a-1,b,memo)+self.memo(a,b-1,memo)
        return memo[key]


s=Solution()
print(s.memo(3,3))