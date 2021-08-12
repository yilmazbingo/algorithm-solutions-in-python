#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curSum=0
        #prefixSum is cumulative sum
        prefixSum={0:1}
        for n in nums:
            curSum+=n
            difference=curSum-k
            # curSum=difference+k, if prefix[diff] exists than means there are some elements equal to "k"
            res+=prefixSum.get(difference,0)
            prefixSum[curSum]=1+prefixSum.get(curSum,0)
        return res

