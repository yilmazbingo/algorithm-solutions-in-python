'''
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.
'''
from TreeNode import TreeNode
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # instead of nonlocal i could use res=[root.val]
        res = root.val
        def dfs(root):
            if not root:
                return 0
            # we recureively go down to the leaf nodes
            left = dfs(root.left)
            right = dfs(root.right)
            # if left or right is negative we do not want to add
            left_max = max(left, 0)
            right_max = max(right, 0)
            # if we split from root we cannot split again
            # compute max with splitting
            nonlocal res
            res = max(root.val + left_max + right_max, res)
            #compute max without splitting. that is what we return to parent
            return root.val + max(left_max, right_max)
        dfs(root)
        return res