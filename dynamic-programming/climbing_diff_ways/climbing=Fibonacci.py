'''
70.Easy Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# at every decision we take one step or two steps
#similar to fibonacci. Draw the decision tree


# create dp and start from the last step. from end and previous, there is only one way to reach top
# in every given point we have 2 decisions to make. we can climb one step or 2 steps. draw the decision tree
# Butoom up solution because we start from base case. each step depends on the prev step
class Solution:
    def climbStairs(self, n: int) -> int:
        # THIS IS FIBONACCI SEQUENCE
        # this is top to bottom approach. in the last and previous we can reach top at one 1 step.
        one,two=1,1
        # since we initialized one,two, we have to comupute only n-1 values.
        for i in range(n-1):
            one,two=two,one+two
        return two

# T :O( 2 ^) n without caching
# T :O(n) with caching