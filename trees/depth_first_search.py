from TreeNode import TreeNode
from typing import List
'''
          a
        /   \
       b      c
     /  \      \
    d    e      f
'''
# INORDER, PREORDER, POSTORDER
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
            # we want to process the left first, so we push the right first then left
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
    def recursive(self,root:TreeNode)->List[int]:
        # this is preorder depth first
        if not root:
            return []
        left_values=self.recursive(root.left) # b,d,e
        right_values=self.recursive(root.right) # c,f
        return [root.val, *left_values,*right_values]
# pre-in-post orders are different flavors of depth first search