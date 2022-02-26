
from List_Node import ListNode
class Solution:
    def swap_pairs(self,head:ListNode):
        dummy=ListNode(0,head)
        prev,cur=dummy,head

        while cur and cur.next:
            # keep the references of next pair and second node to point to the next pair
            next_pair=cur.next.next
            second=cur.next

            # reverse the pair
            second.next=cur
            cur.next=next_pair
            prev.next=second

            # update pointers
            prev=cur
            cur=next_pair
        return dummy.next