# Find if a root to leaf path exists where summation of all elements on the path equals to target.
class TreeNode:
    __slots__='val','left','right'
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def has_path_sum(self,root:TreeNoe,target:int)->bool:
        def dfs(node,target,cur):
            if node is None:
                return False
            cur+=node.val
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