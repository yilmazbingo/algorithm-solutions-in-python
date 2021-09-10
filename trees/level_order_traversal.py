


from TreeNode import TreeNode
from typing import Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=deque()
        queue.append(root)
        while(len(queue)):
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res