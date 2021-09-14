'''
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''



from typing import Optional
from TreeNode import TreeNode
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        inverted_tree=self.invert(root)
        return self.check(root,inverted_tree)
    # compare inverted tree with the original tree
    def check(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1!=None and root2!=None:
            return (root1.val==root2.val) and self.check(root1.left,root2.right) and self.check(root1.right,root2.left)
        return False
    # with preorder, swap the children of each node
    def invert(self,root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invert(root.left)
        self.invert(root.right)
        return root