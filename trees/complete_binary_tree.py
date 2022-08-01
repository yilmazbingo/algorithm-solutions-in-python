'''
222. Medium Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all
nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity. It has to be either o(logN) or O(1)
'''
# Total number of node in full tree 2^(h-1)-1. level of root is 1. So height does not start from 0
# we need to figure out time complexity of "h" value
#Heigh of binary tree is log(N). time complexity of finding h:O(log(N))

from typing import Optional
from TreeNode import TreeNode
def countNodes(self, root: Optional[TreeNode]) -> int:
    # this is preorder and takes O(N)
    # question is asking just count the nodes but with giving Complete Binary tree, it wants us to solve with less than O(N)
    def dfs(node):
        if not node:
            return 0
        return dfs(node.left) + dfs(node.right) + 1
    return dfs(root)
#O(log(N)*log(N))
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # this will count left extreme depth
        def left_height(node):
            if not node: return 0
            return 1+left_height(node.left)
        # this will count right extreme depth
        def right_height(node):
            if not node: return 0
            return 1+right_height(node.right)
        left,right=left_height(root),right_height(root)
        # But if the two depth is not the same, then recursively solve the problem, which is divide, countNodes for the left subtree and the right subtree, sum up and plus 1.
        # we are actually dividing and counting the divisions. because some parts will be perfect binary tree and we will be using the formula
        if left>right:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        else:
            # this is complete balanced tree or perfect binary tree where all positions are filled. left is height here
            return (2**left)-1