#find the kth smallest element in bst. Medium
# if we traverse bst in order and push each element to the array, we get sorted array.
# for iterative solution we need stack to store the visited node's values

# Basic inorder traversal. bst is by default sorted
# inOrder traverses elements in a SORTED FASHION
from typing import Optional
from TreeNode import TreeNode
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=None
        def inorder(node):
            if not node:
                return
            # in bst this is the smallest value
            inorder(node.left)
            # python determines the scope at creation time of the function
            nonlocal k
            k-=1
            if k==0:
                nonlocal res
                res=node.val
                return
            inorder(node.right)
        inorder(root)
        return res