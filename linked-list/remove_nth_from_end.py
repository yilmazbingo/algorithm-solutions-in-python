# remove the nth node from the end
from typing import Optional
from List_Node import ListNode
class Solution:
    def remove(self,head:ListNode,n:int)->ListNode:
        dummy=ListNode(0,head)
        # pay attention that left starts at dummy
        left=dummy
        right=head
        # this makes sure, right is n step ahead of left
        while n>0 and right:
            right=right.next
            n-=1
        # when right reaches the end, left would be the previous of the node that we delete
        # that is why left started at dummy node
        while right:
            left=left.next
            right=right.next
        # now delete it
        left.next=left.next.next
        # return head is not working. WHY?
        return dummy.next
     # https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next

