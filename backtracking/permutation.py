from typing import List
class Solution:
    def best(self,nums:List[int])->List[List[int]]:
        result=[]
        if len(nums)==1:
            # this is way faster than [nums.copy()]. attention, i am returning in array
            return [nums[:]]
        for i in range(len(nums)):
            # pop the each item and get the permutaion of rest
            n=nums.pop(0)
            perms=self.best(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, path):
            if len(nums) == 0:
                result.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return result

    def permutes(self,nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        result = []
        # Iterate the input(lst) and calculate the permutation
        for i in range(len(nums)):
            m = nums[i]
            remaining_list = nums[:i] + nums[i + 1:]
            # Generating all permutations where m is first element
            for p in self.permutes(remaining_list):
                result.append([m] + p)
        return result

s=Solution()
print("best",s.best([1,2,3]))
print(s.permute([1,2,3]))