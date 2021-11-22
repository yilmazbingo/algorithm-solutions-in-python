'''
Given the root of a bst, rearrange the tree in in-order so that the leftmost node in the tree is now the root
of the tree, and every node has no left child and only one right child
'''

from TreeNode import TreeNode

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # with this we dont need to consisder firs time if head is null.
        head =TreeNode("dummy")
        # global cursor
        cursor =head
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            # Python determines the scope of objects at compile-time, not at run-time.
            nonlocal cursor
            cursor.right =TreeNode(node.val)
            cursor =cursor.right
            inorder(node.right)
        inorder(root)
        return head.right



