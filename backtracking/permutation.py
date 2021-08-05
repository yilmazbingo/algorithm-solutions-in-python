from typing import List
class Solution:
    def best(self,nums:List[int])->List[List[int]]:
        result=[]
        if len(nums)==1:
            # this is way faster than [nums.copy()]
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

    def permute(self,nums):
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
            for p in self.permute(remaining_list):
                result.append([m] + p)
        return result

s=Solution()
print("best",s.best([1,2,3]))
print(s.permute([1,2,3]))