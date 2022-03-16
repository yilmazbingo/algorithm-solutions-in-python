# given two binary trees, when you put one of them to cover the other, some nodes overlapped, while others not
# the merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
#Otherwise NOT null node will be used as the node of new tree.

# O(n+m) time because we are traversing

from TreeNode import TreeNode

class Solution:
    def merge(self,root1:TreeNode,root2:TreeNode)->TreeNode:
        # we are going to create a brand new tree
        # we traverse the both tree at exact same time.
        if not root1 and not root2:
            return None
        v1=root1.val if root1 else 0
        v2=root2.val if root2 else 0
        root=TreeNode(v1+v2)
        root.left=self.merge(root1.left if root1 else None,root2.left if root2 else None)
        root.right=self.merge(root1.right if root1 else None,root2.right if root2 else None )
        return root

