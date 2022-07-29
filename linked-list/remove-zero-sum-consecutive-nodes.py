'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
'''
'''
OrderedDict
- supports reverse iteration
- allows us pop first or last item in the dictionary
- move item to the beginning or end of dictionary
- equality comparison is different. keys should be in the same index
- memorywise ordered dict is more performant but for speed, each functionality differs.
'''
from List_Node import ListNode
from collections import OrderedDict

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0,head)
        prefix = 0
        seen = OrderedDict()
        while cur:
            prefix += cur.val
            # if key does not exist, return cur as default
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
