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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode(0,head)
        cur=head
        size=0
        while cur:
            size+=1
            cur=cur.next
        target=size-n
        cur=dummy
        count=0
        while count<target:
            count+=1
            cur=cur.next
        cur.next=cur.next.next
        return dummy.next

