from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1] * len(nums)
        # i starts at 1
        for i in range(1, len(nums)):
            # j starts at 0 till i
            for j in range(i):
                if nums[j] < nums[i]:
                    counts[i] = max(counts[i], counts[j] + 1)
        return max(counts)
