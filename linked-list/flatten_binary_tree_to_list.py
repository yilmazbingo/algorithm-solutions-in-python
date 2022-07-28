# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''
Given the root of a binary tree, flatten the tree into a "linked list":
   The "linked list" should use the same TreeNode class where the right child pointer points to the next node
in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''
from typing import Optional
from trees.TreeNode import TreeNode

def flatten(self, root: Optional[TreeNode]) -> None:
    if not root:
        return None
    stack = []
    stack.append(root)
    while len(stack):
        current_node = stack.pop()
        # we are going to add the right node to the stack first. Becase we need to pop left first
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
        '''
              1
            /  \
           2    5
        we add right first then left. this is in stack [5,2] and current_node is 1
        we want 1.right=2, that is why  current_node.right = stack[-1]
        '''
        if stack:
            current_node.right = stack[-1]
        current_node.left = None
