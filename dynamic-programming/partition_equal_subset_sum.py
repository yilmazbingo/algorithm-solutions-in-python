# https://leetcode.com/problems/partition-equal-subset-sum/
'''
Given a non-empty array nums containing only positive integers, find
if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''
from typing import List
class Solution:
    def canPartition(self, nums):
        total=sum(nums)
        if total%2!=0:
            return False
        t = total/2
        # we have to pass an iterable to set
        P = set([nums[0]])
        for x in nums[1:]:
            for y in list(P):
                P.add(x+y)
        return t in P
    def partition(self,nums:List[int])->bool:
        total=0
        # sum(nums)
        for num in nums:
            total+=num
        if total%2!=0:
            return False
        target=total/2
        store=set()
        # i need to add this to start an iteration. 0 is the base case.
        store.add(0)
        for num in nums:
            # We cannot update store set while we are iterating through it
            # that is why dp.add(s) is added.
            dp=set()
            for s in store:
                if target==s+num:
                    return True
                dp.add(s+num)
                dp.add(s)
            store=dp
        return False



s=Solution()
print(s.partition([3,3,3,4,5]))
