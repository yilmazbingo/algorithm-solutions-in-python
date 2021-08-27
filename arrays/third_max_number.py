from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set()
        for num in nums:
            visited.add(num)
        sorted_nums = sorted(list(visited));
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        return sorted_nums[-3]
