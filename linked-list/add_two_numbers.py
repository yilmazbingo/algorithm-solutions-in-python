'''
2. Add Two Numbers Medium
 You are given two NON-EMPTY linked lists representing two NON-NEGATIVE integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit.
 342= 2 --> 4 -->3
 Add the two numbers and return the sum as a linked list.
'''
from List_Node import ListNode
class Solution:
    def add(self,l1:ListNode,l2:ListNode)->ListNode:
        # it is a starter node
        dummy = ListNode()
        cur = dummy
        carry = 0
        # l1 or l2 is each digit. looks like root node is passed
        # since it is reversed, we start to sum the 1's place. that makes it easier
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            # becayse we are adding digits, if it is 15 carry will be 1
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next