# invert the binary tree.
# root stays same

from treetoy import TreeNode

class Solution:
    def invert(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)
        return root