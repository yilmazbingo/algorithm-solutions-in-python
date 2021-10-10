from typing import List
class Solution:
    def coinChange(self, nums: List[int], target: int) -> int:
        def dfs(target, memo={}):
            if target in memo:
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None
            shortest_combination = None
            for num in nums:
                remainder = target - num
                result = dfs(remainder)
                if result != None:
                    combination = [*result, num]
                    if shortest_combination == None or len(combination) < len(shortest_combination):
                        shortest_combination = combination
            memo[target] = shortest_combination
            return shortest_combination

        return -1 if dfs(target) == None else len(dfs(target))




    # this is slow and has a bad memory usage
    # --- BOTTOM UP -----
    def change(self,target,nums):
        dp = [None for y in range(target + 1)]
        dp[0] = []
        for i in range(len(dp)):
            if dp[i] != None:
                for num in nums:
                    if i + num <= target:
                        # combination=[*dp[i],num]
                        if dp[i + num] == None or len([*dp[i], num]) < len(dp[i + num]):
                            dp[i + num] = [*dp[i], num]

        return len(dp[target]) if dp[-1] != None else -1

    # ---- BOTTOM UP -----
    '''
    we create a dp array that will hold the min number of coins that we need to reach each amount from 1-last
    '''
    def best(self,target,nums):
        dp=[target+1]*(target+1)
        dp[0]=0
        for i in range(1,target+1):
            for num in nums:
                # I add 1 because when I reach here, means i am adding a coin
                dp[i]=min(dp[i],1+dp[i-num])
        return dp[target] if dp[target]!=(target+1) else -1

s=Solution()
print(s.best(11,[1,2,5]))