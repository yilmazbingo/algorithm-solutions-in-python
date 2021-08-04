
from typing import List
class Solution:
    def partition(self,nums:List[int])->bool:
        total=0
        for num in nums:
            total+=num
        print(total)
        if total%2!=0:
            return False
        target=total/2
        store=set()
        store.add(0)
        for num in nums:
            # I cannot mutate a set inside a loop
            dp=set()
            for s in store:
                print(s)
                if target==s+num:
                    return True
                dp.add(s+num)
                dp.add(s)
            store=dp
        return False



s=Solution()
print(s.partition([3,3,3,4,5]))
