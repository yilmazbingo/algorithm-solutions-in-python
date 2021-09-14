# invert the binary tree.
# root stays same

from TreeNode import TreeNode

# take the root and swap the children
# preorder DFS
class Solution:
    def invert(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)
        return root