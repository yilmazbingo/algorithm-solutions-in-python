'''Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.'''
# this code works but too slow for leetcode
import math


class Solution:
    # botom up aproach, big problem n depends on the smaller subproblems. base case is n=0
    # T =O(n * log(N))
    def better(self,n:int)->int:
        dp=[n]*(n+1)
        dp[0]=0
        for target in range(1,n+1):
            for s in range(1,target+1):
                square=s*s
                if target-square<0:
                    break
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]

    def numSquares(self, n: int) -> int:
        if self.is_square(n):
            return 1
        store = []
        # in case n==2
        for i in range(1, n // 2 + 1):
            # if self.is_square(i):
            if i * i < n:
                # a=int(math.sqrt(i))
                store.append(i * i)
                print(store)

        def best_sum(target, nums, memo):
            if len(nums) == 0:
                return []

            if target in memo:
                return memo[target]
            if target == 0:
                return []
            if target < 0:
                return None
            # every recursive call will have its shortest_combination
            shortest_combination = None
            for num in nums:
                remainder = target - num
                result = best_sum(remainder, nums, memo)
                if result != None:
                    # T:O(n * m * len(combination=m) combination might include 1's
                    # Space:O(m * (m+len(memo)) ) stack * len(shortest_cobination)
                    combination = [*result, num]
                    if shortest_combination == None or len(combination) < len(shortest_combination):
                        shortest_combination = combination
            # return value is not inside for loop becasu I cannot return early
            memo[target] = shortest_combination
            return shortest_combination

        return len(best_sum(n, store, {}))

    def is_square(self, n):
        for i in range(1, n + 1):
            if n / i == i:
                return True
        return False
s=Solution()
print(s.numSquares(12))
print(s.numSquares(13))
print(s.better(12))
print(s.better(13))