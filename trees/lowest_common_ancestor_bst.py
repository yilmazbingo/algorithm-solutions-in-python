'''
There must be no duplicate nodes.
The left subtree of a node contains only nodes with keys lesser than the node’s key.
'''

from TreeNode import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # in tree, root is always common ancestor of every single node
        cur=root
        while cur:
            # we are on the right subtree
            if p.val>cur.val and q.val>cur.val:
                cur=cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur=cur.left
            else:
                # when split occurs, that is the lowest common ancestor. it does not matter which one less or greater
                return cur
