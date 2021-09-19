

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # we are looking for dp[4]
        # base case. there is one case to add up to 0
        dp ={0 :1}
        for total in range(1 ,target +1):
            dp[total ] =0
            for n in nums:
                dp[total]+=dp.get(total -n ,0)
        return dp[target]
