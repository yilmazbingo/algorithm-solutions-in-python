# Find if a root to leaf path exists where summation of all elements on the path equals to target.
from TreeNode import TreeNode
class Solution:
    def has_path_sum(self,root:TreeNode,target:int)->bool:
        def dfs(node,target,cur):
            if node is None:
                return False
            cur+=node.val
            # when it hits leaf node, traverse stops
            if cur==target and node.left is None and node.right is None:
                return True
            return dfs(node.left,target,cur) or dfs(node.right,target,cur)
        return dfs(root,target,0)

    # def dfs(self,root:TreeNode,target:int,cur:int)->bool:
    #     if root is None:
    #         return False
    #     cur+=root.val
    #     if cur==target and root.left is None and root.right is None:
    #         return True
    #     return self.dfs(root.left,target,cur) or self.dfs(root.right,target,cur)
    #
    # def has_path_sum(self,root:TreeNoe,target:int)->bool:
    #     return self.dfs(root,target,0)