'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True,0]
            # with recursion, we start from bottom, so we do not have repetitive work
            left,right=dfs(root.left),dfs(root.right)
            balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
            # 1+max(left[1],right[1]) is the height of the each subtree
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]