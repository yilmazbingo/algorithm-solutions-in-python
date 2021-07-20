# this will be solved with BFS-level-order-traversal
#The collection Module in Python provides different types of containers. Counters, OrderedDict,DefaultDict,ChainMap, NamedTuple, DeQue,UserDict,UserList,UserString
# Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
import collections
class Solution:
    def right_view(self,root:TreeNode):
        res=[]
        # deq is faster
        q=collections.deque([root])
        while q:
            right_side=None
            q_length=len(q)
            for i in range(q_length):
                node=q.popleft()
                if node:
                    right_side=node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res