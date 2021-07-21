# Validate Binary Search Treee
# T:O(n*n) with brute force because we are comparing each node with the rest of the nodes
# with DFS T:O(2n) becasue for each node we make only two comparisons

class Solution:
    def is_bst(self,root:TreeNode):
        def dfs(node,left,right):
            if not node:
                return False
            if not (node.val>left and node.val<right):
                return False
            return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)
        return dfs(root, float("-inf"), float("+inf"))
