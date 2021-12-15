'''
 Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with
  even indices,  and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
1 -> 2 -> 3 -> 4 -> 5
1 -> 3 -> 5 -> 2 > 4
'''
def solution(head):
    if not head:
        return head
    odd=head
    even=odd.next
    # this is the beginning of the even list
    even_list=even
    # odd.next=even
    # this makes sure we visit every node
    while odd.next and even.next:
        odd.next=even.next
        odd=odd.next

        even.next=odd.next
        even=even.next
    odd.next=even_list
    return head
