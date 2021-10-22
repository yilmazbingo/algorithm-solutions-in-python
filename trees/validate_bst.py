# Validate Binary Search Tree - Medium
# T:O(n*n) with brute force because we are comparing each node with the rest of the nodes
# with DFS T:O(2n) becasue for each node we make only two comparisons
from TreeNode import TreeNode

# preorder traversal is more helpful.
# we cannot just compare the neighbors because we want to make sure that left tree values are less than root
class Solution:
    def is_bst(self,root:TreeNode):
        if not root:
            return True
        # left and right are boundaries
        def dfs(node,left,right):
            if not node:
                return True
            if not (node.val>left and node.val<right):
                return False
            # when we move right, we update the left, when we move left we update the right
            return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)
        return dfs(root, float("-inf"), float("+inf"))
'''
    -inf < root.val < +inf
when we move to the left, this must holds
    -inf < root.left value  <   root.value
when we move to right
    root.value  < root.right value  < +inf
'''
