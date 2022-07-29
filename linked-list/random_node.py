'''
382. Linked List Random Node
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
'''

import random
from List_Node import ListNode
class Solution:
    def __init__(self, head: ListNode):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        pick = int(random.random() * len(self.range))
        return self.range[pick]
    # random.randint(3, 9) Return a number between 3 and 9 (both included):
    def getRandomInt(self) -> int:
        return self.store[random.randint(0, len(self.store) - 1)]