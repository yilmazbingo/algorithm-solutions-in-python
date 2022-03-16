'''
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

'''

from trees.TreeNode import TreeNode
from typing import Optional
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        store=set()
        def dfs(node):
            if not node:
                return False
            if (k-node.val) in store:
                return True
            store.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)