'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

'''

from typing import List,Optional
from TreeNode import TreeNode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # first element of preorder is root
        root=TreeNode(preorder[0])
        # mid value in inorder gives us root
        mid = inorder.index(preorder[0])
        # we exclude first value from preorder cause it is already taken out for constrcuting root
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root