# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
def solution(head):
    if not head:
        return head
    odd=head
    even=odd.next
    even_list=even
    while odd and even:
        odd.next=even.next
        odd=odd.next

        even.next=odd.next
        even=even.next
    odd.next=even_list
    return head
