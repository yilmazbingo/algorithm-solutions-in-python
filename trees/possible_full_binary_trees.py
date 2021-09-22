'''
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
'''


from TreeNode import TreeNode
from typing import List,Optional
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp={}
        def backtrack(n):
            if n==0:
                return []
            if n==1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            res=[]
            # one is used for root, n-1 for left,right
            for l in range(n):
                r=n-l-1
                left_tree,right_tree=backtrack(l),backtrack(r)
                for t1 in left_tree:
                    for t2 in right_tree:
                        res.append(TreeNode(0,t1,t2))
            dp[n]=res
            return res
        return backtrack(n)