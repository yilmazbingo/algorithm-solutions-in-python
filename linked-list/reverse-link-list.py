
# we are not returning a new linked list. S:O(1)
# we are doing n operations: T: O(N)

# ----------- RECURSIVE SOLUTION ----------
# T:O(N) but S:O(N) as well
# Subproblem is reversing the rest of the linked list

from List_Node import ListNode
class Solution:
    def recursive(self,head:ListNode)->ListNode:
        if not head:
            return None
        new_head=head
        if head.next:
            new_head=self.recursive(head.next)
            head.next.next=head
        head.next=None
        return new_head

    def iterative(head):
        prev = None
        # shift prev to current, shift current to current.next. since this breaks the link, we need to save current.next
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        # at the end of the loop, prev will be the tail
        return prev