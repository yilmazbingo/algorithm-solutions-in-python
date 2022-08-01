'''
894. All Possible Full Binary Trees
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.
'''
from TreeNode import TreeNode
from typing import List,Optional
# T: O(2 ^ n)
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # how many full trees we can create with given n and we cache it
        dp={}
        # returns the full bst with n nodes
        def backtrack(n):
            if n==0:
                return []
            if n==1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            res=[]
            # 1 node is used for root. range does not include n since we use 1 for root, it is ok for us.
            for l in range(n):
                # it is n-1 because in range max number is n-1 not n
                r=n-l-1
                # left_tree and right_tree are list of the fullbst
                left_tree,right_tree=backtrack(l),backtrack(r)
                # if left_tree=[] or right tree=[] this will not run
                # we are going all combinations
                for t1 in left_tree:
                    for t2 in right_tree:
                        # left t1 and right t2
                        res.append(TreeNode(0,t1,t2))
            dp[n]=res
            return res
        return backtrack(n)