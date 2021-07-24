
# we are not returning a new linked list. S:O(1)
# we are doing n operations: T: O(N)

# ----------- RECURSIVE SOLUTION ----------
# T:O(N) but S:O(N) as well
# Subproblem is reversing the rest of the linked list
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
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev