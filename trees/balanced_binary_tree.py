'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
from TreeNode import TreeNode
from typing import Optional

# if I started from root and check each subtree's balanced or not, T would be O(n^2). this is not efficient. because we visit each node more than once
# If i started from bottom, i will visit each node once, so O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # leaf node is balanced
            if not root:
                # we carry the height of each subtree
                return [True,0]
            # with recursion, we start from bottom, so we do not have repetitive work
            left,right=dfs(root.left),dfs(root.right)
            # if any of the subtree return false, then we know entire tree is not balanced
            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            # 1+max(left[1],right[1]) is the height of the each subtree. 1 is the root of the subtree
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]