# if value of each node from path till the node is smaller than node.value, that node is good value
# Return the number of good nodes

from treetoy import TreeNode

class Solution:
    def goodNodes(self,root:TreeNode)->int:
        def dfs(node,max_val):
            if not node:
                return 0
            # in bst there is no duplicate key. equality satisfies if there is only root
            res=1 if node.val >=max_val else 0
            max_val=max(node.val,max_val)
            res+=dfs(node.left,max_val)
            res+=dfs(node.right,max_val)
            return res
        return dfs(root,root.val)