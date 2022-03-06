'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your
maximum jump length at that position. you dont have to jumb lenght of max

Return true if you can reach the last index, or false otherwise.
'''
from typing import List
class Solution:
    def jump(self,nums:List):
        goal=len(nums)-1
        # staring=len(nums)-1 and end at -1 since end is not inclusive, it will stop at the beginning
        for i in range(len(nums)-1,-1,-1):
            # nums[i] is the max jump length. haw mony indices we can jump
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False


s=Solution()
print(s.jump([2,3,1,1,4]))