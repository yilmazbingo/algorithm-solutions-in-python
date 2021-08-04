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
    def optimized(self, nums: List[int], target: int, memo={}) -> int:

        if target in memo:
            return memo[target]

        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            remainder = target - num
            count += self.optimized(nums, remainder)

        memo[target] = count
        return count


class Solution:
    def solve(self, nums, target, memo):
        if target in memo:
            return memo[target]

        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            remainder = target - num
            count += self.solve(nums, remainder, memo)

        memo[target] = count
        return count

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Calling the function
        return self.solve(nums, target, {})


s=Solution()
print(s.unoptimized([9],3))
print(s.optimized([9],3))