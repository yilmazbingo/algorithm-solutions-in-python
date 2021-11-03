'''
101. Symmetric Tree Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

from typing import Optional
from TreeNode import TreeNode
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1,t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return t1.val==t2.val and is_mirror(t1.left,t2.right) and is_mirror(t1.right,t2.left)
        return is_mirror(root.left,root.right)