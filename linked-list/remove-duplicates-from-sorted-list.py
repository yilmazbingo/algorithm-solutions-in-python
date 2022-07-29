from List_Node import ListNode
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        store=dict()
        while head:
            value=head.val
            if value not in store:
                store[value]=head
                head=head.next
                prev=prev.next
            else:
                head=prev.next.next
                prev.next=prev.next.next
        return dummy.next