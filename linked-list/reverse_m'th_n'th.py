'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
'''
from typing import Optional
from List_Node import ListNode
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current_node=head
        start=head
        position=1
        # reaching m-1'th node and keep the reference with start=m-1'th-node
        while position<m:
            start=current_node
            current_node=current_node.next
            position+=1
        # reversing linked list m-n part
        new_list=None
        tail=current_node
        while position>=m and position<=n:
            temp = current_node.next
            current_node.next = new_list
            new_list = current_node
            current_node = temp
            position+=1
        start.next=new_list
        tail.next=current_node
        # if m=1 head will be reversed so I return new_list
        if m>1:
            return head
        else:
            return new_list