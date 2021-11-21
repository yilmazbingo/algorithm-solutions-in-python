'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

'''
# EVERY VALUE IN TREE IS UNIQUE
# Preorder=[root, preorder_of_left,preorder_of_right]
# Inorder= [inorder_of_left, root, inorder_of_right ]
# every value left of root will be in left_subtree, and every value right of root  will be in right_subtree
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
        # we exclude first value from preorder cause it is already taken out for constrcuting root
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]