# invert the binary tree.
# root stays same

from TreeNode import TreeNode

# take the root and swap the children
# preorder DFS
class Solution:
    # TRY THIS WITH INORDER AND POSTORDER AS WELL TO SEE IF WORKS
    def preorder(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.preorder(root.left)
        self.preorder(root.right)
        return root