'''
108. Easy Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''
# they want height balanced because they did not want a skewed tree. it would be easier
# [2,3,4,   5,    7, 10,12   5 is the root, left values are left subtree, right numbers are right subtree
# then take [2,3,4] and create  a tree out of this

#the middle value of the array is the root.
from TreeNode import TreeNode
class Solution:
    def toBST(self,values):
        def dfs(l,r):
            # this happends when l=r=m and we still want to find root.left
            if r<l:
                return None
            m=(l+r)//2
            root=TreeNode(values[m])
            root.left=dfs(l,m-1)
            root.right=dfs(m+1,r)
            return root
        return dfs(0,len(values)-1)