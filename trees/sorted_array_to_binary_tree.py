# Convert the given sorted array into a height balanced BST
'''
 high balanced binary tree is defined as a binary tree in which the depth of two subtrees
 of every node never differs more than 1
'''
#the middle value of the array is the root.
from treetoy import TreeNode
class Solution:
    def toBST(self,values):
        def helper(l,r):
            if l<r:
                return None
            m=(l+r)//2
            root=TreeNode(values[m])
            root.left=helper(l,m-1)
            root.right=helper(m+1,r)
            return root
        return helper(0,len(values)-1)