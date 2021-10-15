# eacht time you can climb 1 or twice
#similar to fibonacci

# Butoom up solution because we start from base case.
# create dp and start from the last step. from end and previous, there is only one way to reach top
# in every given point we have 2 decisions to make. we can climb one step or 2 steps. draw the decision tree
'''
if n=5= dp=[, , , , , 4 ,5]
from 4 and 5, there is only 1 way to reach 5.

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        # since we initialized one,two, we have to comupute only n-1 values.
        for i in range(n-1):
            one,two=two,one+two
        return two

# T :O( 2 ^) n without caching
# T :O(n) with caching