'''
98. Validate Binary Search Tree- Medium
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

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
            # for left subtree, lower-boundary is still -inf, but right boundary is node.val
            return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)
        return dfs(root, float("-inf"), float("+inf"))
'''
    -inf < root.val < +inf
when we move to the left, this must holds
    -inf < root.left value  <   root.value
when we move to right
    root.value  < root.right value  < +inf
'''
