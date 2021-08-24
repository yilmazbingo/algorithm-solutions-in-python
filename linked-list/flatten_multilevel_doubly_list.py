'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own,
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        current_node=head
        while current_node:
            if not current_node.child:
                current_node=current_node.next
            else:
                tail=current_node.child
                while tail.next:
                    tail=tail.next
                tail.next=current_node.next
                if tail.next:
                    tail.next.prev=tail
                current_node.next=current_node.child
                current_node.next.prev=current_node
                current_node.child=None
        return head