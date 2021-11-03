from typing import List
class Solution:
    # we have two pointers. "i" is the beginneing of [0,1,2,1,0] and j at beginnging of [1,2,1]
    def pascal(self,n:int)->List[List[int]]:
        res=[[1]]
        # we start from index-1 because first element is already built [1]
        for i in range(n-1):
            # we assume that in the beginning and end there is 0
            prev=[0]+res[-1]+[0]
            row=[]
            # we add 1  becase res[-1]+[0]
            for j in range(len(res[-1])+1):
                row.append(prev[j]+prev[j+1])
            res.append(row)
        return res


s=Solution()
print(s.pascal(4))