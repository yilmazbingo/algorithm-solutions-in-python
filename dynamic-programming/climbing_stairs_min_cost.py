"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.
Once you pay the cost for a step , you can either climb one or two steps.
Find the minimum cost to reach the top of the staircase. Your first step can either be the first or second step.
"""
from typing import List
def min_cost(i:int,cost:List[int])->int:
    if i<0:
        return 0
    if i==0 or i==1:
        return cost[i]
    return cost[i]+min(min_cost(i-1,cost),min_cost(i-2,cost))

def min_cost_climbing(cost:List[int])->int:
    n=len(cost)
    return min(min_cost(n-1,cost),min_cost(n-2,cost))

print(min_cost_climbing([1, 4, 22, 11, 22]))

