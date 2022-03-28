# Find if a root to leaf path exists where summation of all elements on the path equals to target.
# https://leetcode.com/problems/path-sum/

from TreeNode import TreeNode
class Solution:
    def has_path_sum(self,root:TreeNode,target:int)->bool:
        def dfs(node,cur):
            if node is None:
                return False
            cur+=node.val
            # when it hits leaf node, traverse stops
            if cur==target and node.left is None and node.right is None:
                return True
            return dfs(node.left,cur) or dfs(node.right,cur)
        return dfs(root,0)

