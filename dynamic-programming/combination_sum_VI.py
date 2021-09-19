'''
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.
'''

from typing import List
## leet code did not accep it because of default value
class Solution:
    def unoptimized(self, nums: List[int], target: int,) -> int:

        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            remainder = target - num
            count += self.unoptimized(nums, remainder)
        return count

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Calling the function

        def solve(target, memo):
            if target in memo:
                return memo[target]
            if target == 0:
                return 1
            if target < 0:
                return 0
            count = 0
            for num in nums:
                remainder = target - num
                count += solve(remainder, memo)

            memo[target] = count
            return count

        return solve(target, {})






s=Solution()
print(s.unoptimized([9],3))
print(s.optimized([9],3))