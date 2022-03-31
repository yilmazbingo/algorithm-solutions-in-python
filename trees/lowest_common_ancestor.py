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
        # if current node one of the two target nodes. we return it to up the tree
        if root.val==p.val or root.val==q.val:
            return root
        # we need to search the left/right subtrees for every node in search for our 2 target nodes
        # If we find one at each subtree, the current node is the LCa
        # each call asks what is the LCA from this node
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        # we did not find answer
        if left is None and right is None:
            return None
        # we found both nodes
        if left and right:
            return root
        # if one of them was valid, return the valid one
        if left is None:
            return right
        return left
