'''
236.Medium Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
# time complexity is the O(Log(n)) height of the tree. Because we are visiting only one node for each level
from TreeNode import TreeNode

class Solution:
    # this is postorder traversal. Bottom up
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        # tell that on this side I found p or q
        if root.val==p.val or root.val==q.val:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left is None and right is None:
            return None
        if left and right:
            return root
        if left is None:
            return right
        return left
