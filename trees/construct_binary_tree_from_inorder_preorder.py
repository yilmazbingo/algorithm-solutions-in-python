'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
# EVERY VALUE IN TREE IS UNIQUE
# Preorder=[root, preorder_of_left,preorder_of_right]
# Inorder= [inorder_of_left, root, inorder_of_right ]
# In the inorder traversal, the root is visited after visiting its left subtree but before visiting the right subtree.
# In the preorder traversal, the root is visited before the left and right subtrees are visited (in that order).
from typing import List,Optional
from TreeNode import TreeNode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # first element of preorder is root
        root=TreeNode(preorder[0])
        # mid value in inorder gives us root. left values of root will be the left subtree, right values will be the right subtree
        # mid tells us how many elements we want from left subtree and howmany for right subtree
        mid = inorder.index(preorder[0])
        # we took 1 out of each array. preorder will not include the first, inorder will not include the mid value
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]