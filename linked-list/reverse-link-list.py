
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
        current = head
        prev = None
        # shift prev to current, shift current to current.next. since this breaks the link, we need to save current.next
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        # at the end of the while loop, prev will the new head
        # if i did not set the temp, current.next would no longer points to the next node in linked list
            current.next=prev
            prev= current
            current.next
        return prev