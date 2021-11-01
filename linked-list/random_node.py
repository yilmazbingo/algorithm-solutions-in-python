'''
382. Linked List Random Node
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