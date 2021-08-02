# given an array of numbers find the best combination of numbers to find the target
# similar to coin change

class Solution:
    def best_sum(self,target,nums):
        if target==0:
            return []
        if target<0:
            return None
        # every recursive call will have its shortest_combination
        shortest_combination=None
        for num in nums:
            remainder=target-num
            result=self.best_sum(remainder,nums)
            if result!=None:
                # T:O(n^m * len(combination=m) combination might include 1's
                # Space:O(m * m ) stack * len(shortest_cobination)
                combination=[*result,num]
                if shortest_combination==None or len(combination)<len(shortest_combination):
                    shortest_combination=combination
        return shortest_combination

    def memoized(self,target,nums,memo):
        if target in memo:
            return memo[target]
        if target==0:
            return []
        if target<0:
            return None
        # every recursive call will have its shortest_combination
        shortest_combination=None
        for num in nums:
            remainder=target-num
            result=self.memoized(remainder,nums,memo)
            if result!=None:
                # T:O(n * m * len(combination=m) combination might include 1's
                # Space:O(m * (m+len(memo)) ) stack * len(shortest_cobination)
                combination=[*result,num]
                if shortest_combination==None or len(combination)<len(shortest_combination):
                    shortest_combination=combination
        # return value is not inside for loop becasu I cannot return early
        memo[target]=shortest_combination
        return shortest_combination