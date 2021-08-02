class Solution:
    def sum(self,target, nums):
        # for each element, we ask if generating this element is possible
        # if i just return empty array, that i means i generate sum=0
        dp = [False for y in range(target + 1)]
        # base case in resurcion is called seed value in tabulation
        dp[0] = True
        for i in range(target):
            # if current element is reachable
            if dp[i] == True:
                for num in nums:
                    if i + num <= target:
                        dp[i + num] = True
        return dp[-1]

s=Solution()
print(s.sum(7,[2,3,4]))