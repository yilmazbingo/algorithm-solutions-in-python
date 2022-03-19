# this will be solved with BFS-level-order-traversal
#The collection Module in Python provides different types of containers. Counters, OrderedDict,DefaultDict,ChainMap, NamedTuple, DeQue,UserDict,UserList,UserString
'''
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
'''
from collections import deque
from TreeNode import TreeNode
from typing import Optional,List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = deque([root])
        # queue.append(root)
        res = []
        while len(queue) > 0:
            right = None
            for i in range(len(queue)):
                current = queue.popleft()
                right = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # from right wiev we can only see the last element
            res.append(right)
        return res
