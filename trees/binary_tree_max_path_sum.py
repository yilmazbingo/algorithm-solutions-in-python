'''
124. HARD Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.
'''
# O(n) becasue we are looking each node once. S:O(h) which is log(N) because it is balanced tree
from TreeNode import TreeNode
from typing import Optional
# path means we cannot tsplit twice if we split from root we cannot split again
'''
from each node, we are computing 2 values. 
1- what is the max sum, if we are allowed to split. then we ask its children, what is the max we can get without splitting. this is not the value that i return parent. the reaoson I
compute this, so I could update the result
2- we are going to 
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # instead of nonlocal i could use res=[root.val]
        res = root.val
        def post_order(root):
            if not root:
                return 0
            # we recureively go down to the leaf nodes. POST-ORDER traversal
            left = post_order(root.left)
            right = post_order(root.right)
            # if left or right is negative we do not want to add, we ignore it, so we hand 0 to root
            left_max = max(left, 0)
            right_max = max(right, 0)
            # if we split from root we cannot split again
            # compute max with splitting to update the res
            nonlocal res
            res = max(root.val + left_max + right_max, res)
            # compute max without splitting. that is what we return to parent. we choose the max
            # we are starting from bottom, calculating max we can get from a node and pass it to parent
            return root.val + max(left_max, right_max)
        post_order(root)
        return res