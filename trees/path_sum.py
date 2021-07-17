# Find if a root to leaf path exists where summation of all elements on the path equals to target.
from treetoy import TreeNode
class Solution:
    def has_sum(self,root:TreeNode,target:int,cur:int)->bool:
        if root is None:
            return False
        cur+=root.val
        if cur==target and root.left is None and root.right is None:
            return True
        return self.has_sum(root.left,target,cur) or self.has_sum(root.right,target,cur)

    def has_path_sum(self,root:TreeNoe,target:int)->bool:
        return self.has_sum(root,target,0)