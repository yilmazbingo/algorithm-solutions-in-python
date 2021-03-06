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
        if len_A >len_B:
            long_list =headA
            short_list =headB
            diff =len_A -len_B
        # If I used if instead of else here I would get "local variable referenced before assignment "
        # This will make sure that even if none of your if statements evaluate to True, you can still set a value for the variable with which you are going to work.
        else:
            long_list =headB
            short_list =headA
            diff =len_B -len_A
        i=0
        while i<diff:
            long_list=long_list.next
            i+=1
        # at this point we are at the same level. so if we take a step from each we will reach to the intersection
        while long_list!=short_list:
            long_list=long_list.next
            short_list=short_list.next
        return long_list

    class Solutionn:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            curA = headA
            curB = headB
            lenA = 0
            while curA:
                curA = curA.next
                lenA += 1
            lenB = 0
            while curB:
                curB = curB.next
                lenB += 1
            if lenA < lenB:
                # notice shortest and longest are equal to the head values not curA or curB
                shortest = headA
                longest = headB
            else:
                shortest = headB
                longest = headA
            diff = abs(lenA - lenB)
            while diff:
                longest = longest.next
                diff -= 1
            while longest != shortest:
                longest = longest.next
                shortest = shortest.next
            return shortest
