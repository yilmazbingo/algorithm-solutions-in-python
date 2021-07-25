# Merge two sorted linked lists and return in as a new sorted list.
# each list might be different size

class Solution:
    def merge(self,l1:ListNode,l2:ListNode)->ListNode:
        # this is the node that points to the beginning of the merged list.
        dummy=ListNode()
        # while we traverse we still have to keep the reference of dummy
        tail=dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        # after while loop, one of them might not reach the end but one is not
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        return dummy.next