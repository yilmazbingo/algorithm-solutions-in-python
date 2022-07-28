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
    def flatten(self, head: Node) -> Node:
        if not head:
            return None
        cur=head
        while cur:
            if not cur.child:
                cur=cur.next
            else:
                tail=cur.child
                # our goal is to reach the last node
                while tail.next:
                    tail=tail.next
                tail.next=cur.next
                # tail.next could be None
                if tail.next:
                    tail.next.prev=tail
                cur.next=cur.child
                cur.next.prev=cur
                cur.child=None
        return head