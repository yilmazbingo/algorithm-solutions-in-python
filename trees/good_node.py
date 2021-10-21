'''
1448.Medium Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

from TreeNode import TreeNode
# T:O(N) S:(h)
# Using preorder traversal. root node count as good node
class Solution:
    def goodNodes(self,root:TreeNode)->int:
        def dfs(node,max_val):
            if not node:
                return 0
            # in bst there is no duplicate key. if there is only root, root is counted as a good node
            res=1 if node.val >=max_val else 0
            max_val=max(node.val,max_val)
            res+=dfs(node.left,max_val)
            res+=dfs(node.right,max_val)
            return res
        return dfs(root,root.val)