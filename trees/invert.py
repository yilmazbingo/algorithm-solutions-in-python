# invert the binary tree.
# root stays same

from TreeNode import TreeNode
from typing import Optional
# take the root and swap the children
# preorder DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(node):
            if node:
                node.left,node.right=node.right,node.left
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return root