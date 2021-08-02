
# m=target   n=len(sum)
# since I copy over the array to the new position it also takes m time for worst case
# T: O(m*n*m)
# since len(dp)=m and we store an array insdie dp[i]. len(dp[i]) could be m too
# S:O(m*m)
class Solution:
    def sum(self,target, nums):
        dp = [None for i in range(target + 1)]
        dp[0] = []
        for i in range(len(dp)):
            if dp[i] != None:
                for num in nums:
                    if (i + num <= target):
                        dp[i + num] = [*dp[i], num]
        #     print(dp[-1])
        return dp[-1]

s=Solution()
print(s.sum(7, [3, 4, 5]))