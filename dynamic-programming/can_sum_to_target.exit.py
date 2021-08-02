#given an array of of positive numbers, find if any to can reach to target

class Solution:
    def brute(self,target,nums):
        if target==0:
            return True
        if target<0:
            return False
        for num in nums:
            # if target is larger, it will make a lot of substraction
            # So depth of tree depends on the target. if target-1 we would have m calculatiosn
            # height of tree is m
            # branching is len(nums)=n. for each branch we make m recursive calls:
            # time complexity is o (n over m)
            # Space complexity would be O(height) O(m)
            remainder=target-num
            if self.brute(remainder,nums):
                return True
        return False
    # T: O(m*n)
    def memoied(self,target,nums,memo={}):
        #  before i used to call m recursion for each branch n
        #now i am not memoizing so i dont go deeper
        if target in memo:
            return memo[target]
        if target==0:
            return True
        if target<0:
            return False
        for num in nums:
            remainder=target-num
            if self.memoied(remainder,nums,memo):
                memo[target]=True
                return True
        memo[target]=False
        return False

s=Solution()
s.memoied(300,[7,14])
# memoization will work because 300-7-7 will be stored which is result for 300-14 for the next check