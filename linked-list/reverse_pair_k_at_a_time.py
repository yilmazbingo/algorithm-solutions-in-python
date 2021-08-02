#given k means group the linked list by k and then reverse it

from List_Node import ListNode
class Solution:
    def reverse_kth(self,head:ListNode,k:int)->ListNode:
        # create dumy node and point to the head
        dummy=ListNode(0,head)
        group_prev=dummy
        while True:
            kth=self.get_kth(group_prev,k)
            # if I cannot partition the last part, break out of the loop
            if not kth:
                break
            group_next=kth.next
            #reversing the group with two pointer
            # 1-2---kth  --- kth.next  we dont want to break the link
            prev, cur=kth.next,group_prev.next
            while cur!=group_next:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            #  this temp is the first node in the group
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp
        return dummy.next
    # partition the linked list
    def get_kth(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur
