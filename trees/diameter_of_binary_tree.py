'''
543. Easy Diameter of Binary Tree
COUNTING THE EDGES
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of EDGES between them NOT NODES.
'''
# NODES=EDGES+1

from TreeNode import TreeNode
from typing import Optional
class Solution:
    def DiameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        # with recursion we start from bottom to top. so we visit each node once so T:O(N)
        def post_order(root):
            if not root:
                # height of null tree is -1
                return -1
            # start from bottom
            left=post_order(root.left)
            right=post_order(root.right)
            nonlocal res
            # in reality height of a null tree, by convention is -1. because height of tree with single node is 0
            # that is why we add 1+1=2
            # Diameter=left+right
            res=max(res,1+left+1+right)
            # max(left,right)+1 is the height of each node
            return 1+max(left,right)
        post_order(root)
        return res