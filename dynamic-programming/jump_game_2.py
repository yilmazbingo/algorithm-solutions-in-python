'''
45.Medium Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
'''
# Greedy solution
[2,3,1,1,4]
from typing import List
class Solution:
    def jump(self,nums:List[int])->int:
        res=0
        l,r=0,0
        # to run the last step, we iterate till the previous of the last item
        while r<len(nums)-1:
            # farthest is the index
            farthest=0
            # after first jump, we get a new window. we iterate through here and check how far we can jump from here
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res