# Given a binary tree containing digits 0-9, each root-to-leaf path could represnet a number.
# find the total sum of the all root-to-leaf numbers

class Solution:
    def sum_numbers(self,root:Treenode):
        def dfs(cur_node,sum):
            if not cur_node:
                return 0
            sum=sum*10+cur_node.val
            if not cur_node.left and cur_node.right:
                return sum
            dfs(cur_node.left,sum)+dfs(cur_node.right,sum)
        return dfs(root,0)