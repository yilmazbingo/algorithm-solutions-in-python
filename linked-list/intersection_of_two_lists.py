'''
Easy- Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
'''
from List_Node import ListNode
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_A,cur_B =headA,headB
        len_A =0
        while cur_A:
            cur_A =cur_A.next
            len_A+=1
        len_B =0
        while cur_B:
            cur_B =cur_B.next
            len_B+=1
        # So far found the length of both linked lists
        # Now decide which one is short_list or long_list
        if len_A >len_B:
            long_list =headA
            short_list =headB
            diff =len_A -len_B
        else:
            long_list =headB
            short_list =headA
            diff =len_B -len_A
        i=0
        while i<diff:
            long_list=long_list.next
            i+=1
        # at this point we are at the same level of both l inked lists
        while long_list!=short_list:
            long_list=long_list.next
            short_list=short_list.next
        return long_list
