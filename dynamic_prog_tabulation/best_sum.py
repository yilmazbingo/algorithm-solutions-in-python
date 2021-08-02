class Solution(object):

    def best_sum(self, target, nums):
        dp = [None for y in range(target + 1)]
        dp[0] = []
        for i in range(len(dp)):
            if dp[i] != None:
                for num in nums:
                    if i + num <= target:
                        combination = [*dp[i], num]
                        # combination=dp[i]+[num]
                        if dp[i + num] == None or len(combination) < len(dp[i + num]):
                            dp[i + num] = combination
        return dp[-1]

s=Solution()
print(s.best_sum(11,[1,2,5]))