from collections import deque
from TreeNode import TreeNode
from typing import List
'''
          a
        /   \
       b      c
     /  \      \
    d    e      f
'''
class Solution:
    # we go left as far as we can, iw we cannot go left, we go right, if we cannot go right we are gonna backtrack
    def dfs(self,root:TreeNode)->List[int]:
        if not root:
            return []
        res=[]
        stack=[]
        stack.append(root)
        while len(stack)>0:
            current_node=stack.pop()
            res.append(current_node.val)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
    def recursive(self,root:TreeNode)->List[int]:
        if not root:
            return []
        left_values=self.recursive(root.left) # b,d,e
        right_values=self.recursive(root.right) # c,f
        return [root.val, *left_values,*right_values]