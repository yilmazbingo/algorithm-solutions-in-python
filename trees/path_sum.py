# Find if a root to leaf path exists where summation of all elements on the path equals to target.
# https://leetcode.com/problems/path-sum/

from TreeNode import TreeNode
class Solution:
    def has_path_sum(self,root:TreeNode,target:int)->bool:
        def preorder(node,cur):
            if node is None:
                return
            cur+=node.val
            # when it hits leaf node, traverse stops
            if cur==target and node.left is None and node.right is None:
                return True
            return preorder(node.left,cur) or preorder(node.right,cur)
        return preorder(root,0)

