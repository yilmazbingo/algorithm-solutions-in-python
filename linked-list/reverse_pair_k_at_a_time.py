# https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
from List_Node import ListNode
class Solution:
    def reverse_kth(self,head:ListNode,k:int)->ListNode:
        # we are potentially modifying the head of list
        dummy=ListNode(0,head)
        # we always gonna save one node right before the group
        group_prev=dummy
        while True:
            kth=self.get_kth(group_prev,k)
            # if I cannot partition the last part, break out of the loop
            if not kth:
                break
            # keep track of node right after our group
            group_next=kth.next
            #reversing the group with two pointer
            # 1-2---kth  --- kth.next  we dont want to break the link
            # usually when we use prev=None, None is used because after traversing head would be tail and would point to None.
            prev=kth.next
            cur=group_prev.next
            while cur!=group_next:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            #  1 -> 2 -> 3 -> 4 group_prev was dummy. now it should be 1
            #  2 -> 1 -> 4 -> 3  group_prev.next was 1, not it should be 2.
            # this temp is not related to the above temp
            temp=group_prev.next
            # one node before our group .next is now kth
            group_prev.next=kth
            group_prev=temp
        return dummy.next
    # partition the linked list
    def get_kth(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur
