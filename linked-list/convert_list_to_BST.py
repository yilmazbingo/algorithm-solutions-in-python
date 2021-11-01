'''
109. Convert Sorted List to Binary Search Tree
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
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow=fast=head
        pre=ListNode()
        # we use slow and fast pointer to find the middle node to create the head of tree
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        # slow will be middle, and pre will be pre -> slow
        # we need to cut this pointer, because we are recursively calling on the left
        # if I dont cut it, when I recursively do while loop in left side, it would loop through entire linked list
        pre.next=None
        root=TreeNode(slow.val)
        # we pass the beginner of left and right side
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(slow.next)
        return root