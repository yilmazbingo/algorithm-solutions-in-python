# remove the nth node from the end

class Solution:
    def remove(self,head:ListNode,n:int)->ListNode:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        # this makes sure, right n step ahead of left
        while n>0 and right:
            right=right.next
            n-=1
        # when right reaches the end, left would be the previous of the node that we delete
        while right:
            left=left.next
            right=right.next
        # now delete it
        left.next=left.next.next
        return dummy.next

