# [1] [2] [3] [4]
# if we decide to rob the first house rob=max(arr[0]+rob[2:n])
# if we skip the first house rob=max(rob[1:n])

from typing import List
class Solution:
    def rob(self,nums:List[int])->int:
        rob1,rob2=0,0
        # [rob1,rob2,n,n+1, ...]
        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
