
from typing import List
from collections import deque
from TreeNode import TreeNode
class Solution:
    # T:O(n) if removing and adding in queue takes constant time
    # S:O(N)
    def breadth(self,root:TreeNode)->List[int]:
        if not root:
            return []
        res=[]
        queue=deque()
        queue.append(root)
        while len(queue)>0:
            current_node=queue.popleft()
            res.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return res

