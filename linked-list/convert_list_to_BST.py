'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
 of every node never differ by more than 1.
'''

# mid node of the linked list will be the head. then recursively find the mid point of other parts and make them  head

from typing import Optional
from List_Node import ListNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size=0
        current=head
        root=head
        while current:
            current=current.next
            size+=1
        # this has to be global
        self.head=head
        def dfs(start,end):
            if start>end:
                return None
            # build left subtree
            mid=(start+end)//2
            # this dfs will keep calculating left head
            left=dfs(start,mid-1)
            # define root
            root=TreeNode(self.head.val)
            self.head=self.head.next
            root.left=left
            root.right=dfs(mid+1,end)
            return root
        return dfs(0,size-1)