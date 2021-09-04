
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
            nonlocal res
            res = max(root.val + left_max + right_max, res)
            return root.val + max(left_max, right_max)
        dfs(root)
        return res