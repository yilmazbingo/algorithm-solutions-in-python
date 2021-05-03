def reverse(head):
    current=head
    prev=None
    while current:
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev
# we are not returning a new linked list. S:O(1)

# we are doing n operations: T: O(N)