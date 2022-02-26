 #148.Given the head of a linked list, return the list after sorting it in ascending order in O(N log(N))
# Merge sort is a recursive algorithm. dividing takes log(N) and comparing takes N

from typing import Optional
from List_Node import ListNode
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        left,right=head,self.get_middle(head)
        # Second half should be starting with right.next, not right
        # when we divide the list into 2, tail of each part will point to None
        temp=right.next
        # this is important state. self.sortlist(left) will call it self and its tail will be updated
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)

    def get_middle(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

    def merge(self, left,right):
        tail=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next
