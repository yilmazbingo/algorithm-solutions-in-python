# return the elements that reaches the target, if  not return null


class Solution:
    def pairs(self,target,nums):
        if target==0:
            return []
        if target<0:
            return None
        for num in nums:
            remainder=target-num
            return_result=self.pairs(remainder,nums)
            if return_result!=None:
                # in the worst case array can include m elements.1+1+1+1+1
                # this line creates a copy array, which will take m time.
                # O:T=O(n^m * m) m is target,n is len(nums)
                # I am making O(n^m) recursive call and each call calculate the spread operation
                # spcae O(m+m)
                return [*return_result,num]
        return False
    # T:O(n*m*n) m*n is recursive calls times m spreading array
    def memo(self,target, nums, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return []
        if target < 0:
            return None
        for num in nums:
            remainder = target - num
            return_result = self.memo(remainder, nums, memo)
            if return_result != None:
                memo[target] = [*return_result, num]
                return memo[target]
        memo[target] = False
        print(memo)
        return False