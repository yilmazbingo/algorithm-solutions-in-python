''' Medium https://leetcode.com/problems/sum-root-to-leaf-numbers/
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
'''

from TreeNode import TreeNode
class Solution:
    def sumNumbers(self,root:TreeNode):
        # preorder. processing the
        def dfs(cur_node,num):
            if not cur_node:
                return 0
            num=num*10+cur_node.val
            # if this is a leaf node
            if not cur_node.left and not cur_node.right:
                return num
            return dfs(cur_node.left,num)+dfs(cur_node.right,num)
        # we pass 0 zero because we calculate the num 10*0+root.val
        return dfs(root,0)